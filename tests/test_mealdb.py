import unittest
import unittest.mock
import httpx

from py_mealdb import MealDB
from py_mealdb.models import MealDetails, MealList, CategoryList, AreaList, IngredientList
from unittest.mock import Mock, patch, mock_open


class TestMealDB(unittest.TestCase):

    def setUp(self):
        self.api_key = 1
        self.meal_db = MealDB(self.api_key)

    # ─────────────────────────────────────────
    # get_meal_by_name
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_get_meal_by_name_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [
            {'idMeal': '52772', 'strMeal': 'Arrabiata'},
            {'idMeal': '52773', 'strMeal': 'Arrabiata Sauce'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.get_meal_by_name('Arrabiata')
        self.assertIsInstance(response, MealDetails)
        self.assertGreater(len(response), 0)
        self.assertIn('Arrabiata', response.names)
        self.assertIn('Arrabiata Sauce', response.names)

    @patch('httpx.get')
    def test_get_meal_by_name_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.get_meal_by_name('NonExistentMeal')
        self.assertIsInstance(response, MealDetails)

    @patch('httpx.get')
    def test_get_meal_by_name_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.get_meal_by_name('Arrabiata')

    @patch('httpx.get')
    def test_get_meal_by_name_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "404 Not Found", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.get_meal_by_name('Arrabiata')

    # ─────────────────────────────────────────
    # meal_details_by_id
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_meal_details_by_id_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Arrabiata'}]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.meal_details_by_id('52772')
        self.assertIsInstance(response, MealDetails)
        self.assertGreater(len(response), 0)
        self.assertEqual(response[0]['idMeal'], '52772')
        self.assertEqual(response[0]['strMeal'], 'Arrabiata')

    @patch('httpx.get')
    def test_meal_details_by_id_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.meal_details_by_id('99999')
        self.assertIsInstance(response, MealDetails)

    @patch('httpx.get')
    def test_meal_details_by_id_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.meal_details_by_id('52772')

    @patch('httpx.get')
    def test_meal_details_by_id_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "404 Not Found", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.meal_details_by_id('52772')

    # ─────────────────────────────────────────
    # single_random_meal
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_single_random_meal_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Random Meal'}]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.single_random_meal()
        self.assertIsInstance(response, MealDetails)
        self.assertGreater(len(response), 0)
        self.assertEqual(response[0]['strMeal'], 'Random Meal')

    @patch('httpx.get')
    def test_single_random_meal_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.single_random_meal()
        self.assertIsInstance(response, MealDetails)


    @patch('httpx.get')
    def test_single_random_meal_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.single_random_meal()

    @patch('httpx.get')
    def test_single_random_meal_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.single_random_meal()

    # ─────────────────────────────────────────
    # list_all_meals
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_list_all_meals_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [
            {'idMeal': '52772', 'strMeal': 'Apple Pie'},
            {'idMeal': '52773', 'strMeal': 'Avocado Toast'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all_meals('a')
        self.assertIsInstance(response, MealDetails)
        self.assertGreater(len(response), 0)
        self.assertIn('Apple Pie', response.names)
        self.assertIn('Avocado Toast', response.names)

    @patch('httpx.get')
    def test_list_all_meals_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all_meals('z')
        self.assertIsInstance(response, MealDetails)
        self.assertEqual(len(response), 0)

    @patch('httpx.get')
    def test_list_all_meals_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.list_all_meals('a')

    @patch('httpx.get')
    def test_list_all_meals_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.list_all_meals('a')

    # ─────────────────────────────────────────
    # list_meal_categories
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_list_meal_categories_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'categories': [
            {'idCategory': '1', 'strCategory': 'Beef'},
            {'idCategory': '2', 'strCategory': 'Chicken'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_meal_categories()
        self.assertIsInstance(response, CategoryList)
        self.assertGreater(len(response), 0)
        self.assertIn('Beef', response.categories)
        self.assertIn('Chicken', response.categories)

    @patch('httpx.get')
    def test_list_meal_categories_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'categories': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_meal_categories()
        self.assertIsInstance(response, CategoryList)

    @patch('httpx.get')
    def test_list_meal_categories_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.list_meal_categories()

    @patch('httpx.get')
    def test_list_meal_categories_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.list_meal_categories()

    # ─────────────────────────────────────────
    # list_all_categories
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_list_all_categories_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'categories': [
            {'strCategory': 'Beef'},
            {'strCategory': 'Chicken'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all_categories()
        self.assertIsInstance(response, CategoryList)
        self.assertGreater(len(response), 0)
        self.assertIn('Beef', response.categories)
        self.assertIn('Chicken', response.categories)

    @patch('httpx.get')
    def test_list_all_categories_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'categories': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all_categories()
        self.assertIsInstance(response, CategoryList)

    @patch('httpx.get')
    def test_list_all_categories_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.list_all_categories()

    @patch('httpx.get')
    def test_list_all_categories_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.list_all_categories()

    # ─────────────────────────────────────────
    # list_all_areas
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_list_all_areas_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [
            {'strArea': 'Mexican'},
            {'strArea': 'Canadian'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all_areas()
        self.assertIsInstance(response, AreaList)
        self.assertGreater(len(response), 0)
        self.assertIn('Mexican', response.areas)
        self.assertIn('Canadian', response.areas)

    @patch('httpx.get')
    def test_list_all_areas_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all_areas()
        self.assertIsInstance(response, AreaList)

    @patch('httpx.get')
    def test_list_all_areas_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.list_all_areas()

    @patch('httpx.get')
    def test_list_all_areas_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.list_all_areas()

    # ─────────────────────────────────────────
    # list_all_ingredients
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_list_all_ingredients_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [
            {'idIngredient': '1', 'strIngredient': 'Chicken'},
            {'idIngredient': '2', 'strIngredient': 'Beef'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all_ingredients()
        self.assertIsInstance(response, IngredientList)
        self.assertGreater(len(response), 0)
        self.assertIn('Chicken', response.ingredients)
        self.assertIn('Beef', response.ingredients)

    @patch('httpx.get')
    def test_list_all_ingredients_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all_ingredients()
        self.assertIsInstance(response, IngredientList)

    @patch('httpx.get')
    def test_list_all_ingredients_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.list_all_ingredients()

    @patch('httpx.get')
    def test_list_all_ingredients_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.list_all_ingredients()

    # ─────────────────────────────────────────
    # list_all
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_list_all_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            'meals': [{'strArea': 'American'}],
            'categories': [{'strCategory': 'Beef'}],
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.list_all()
        self.assertIsInstance(response, dict)
        self.assertIn('categories', response)
        self.assertIn('areas', response)
        self.assertIn('ingredients', response)
        self.assertIsInstance(response['categories'], CategoryList)
        self.assertIsInstance(response['areas'], AreaList)
        self.assertIsInstance(response['ingredients'], IngredientList)

    @patch('httpx.get')
    def test_list_all_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.list_all()

    @patch('httpx.get')
    def test_list_all_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.list_all()

    # ─────────────────────────────────────────
    # filter_by_ingredient
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_filter_by_ingredient_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [
            {'idMeal': '52772', 'strMeal': 'Chicken Curry', 'strMealThumb': 'https://example.com/image.jpg'},
            {'idMeal': '52773', 'strMeal': 'Chicken Soup', 'strMealThumb': 'https://example.com/image2.jpg'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.filter_by_ingredient('Chicken')
        self.assertIsInstance(response, MealList)
        self.assertGreater(len(response), 0)
        self.assertIn('52772', response.ids)
        self.assertIn('Chicken Curry', response.names)

    @patch('httpx.get')
    def test_filter_by_ingredient_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.filter_by_ingredient('NonExistentIngredient')
        self.assertIsInstance(response, MealList)

    @patch('httpx.get')
    def test_filter_by_ingredient_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.filter_by_ingredient('Chicken')

    @patch('httpx.get')
    def test_filter_by_ingredient_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.filter_by_ingredient('Chicken')

    # ─────────────────────────────────────────
    # filter_by_category
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_filter_by_category_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [
            {'idMeal': '52772', 'strMeal': 'Salmon', 'strMealThumb': 'https://example.com/image.jpg'},
            {'idMeal': '52773', 'strMeal': 'Tuna', 'strMealThumb': 'https://example.com/image2.jpg'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.filter_by_category('Seafood')
        self.assertIsInstance(response, MealList)
        self.assertGreater(len(response), 0)
        self.assertIn('Salmon', response.names)
        self.assertIn('Tuna', response.names)

    @patch('httpx.get')
    def test_filter_by_category_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.filter_by_category('NonExistentCategory')
        self.assertIsInstance(response, MealList)

    @patch('httpx.get')
    def test_filter_by_category_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.filter_by_category('Seafood')

    @patch('httpx.get')
    def test_filter_by_category_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.filter_by_category('Seafood')

    # ─────────────────────────────────────────
    # filter_by_area
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_filter_by_area_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [
            {'idMeal': '52772', 'strMeal': 'Poutine', 'strMealThumb': 'https://example.com/image.jpg'},
            {'idMeal': '52773', 'strMeal': 'BeaverTails', 'strMealThumb': 'https://example.com/image2.jpg'}
        ]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.filter_by_area('Canadian')
        self.assertIsInstance(response, MealList)
        self.assertGreater(len(response), 0)
        self.assertIn('Poutine', response.names)
        self.assertIn('BeaverTails', response.names)

    @patch('httpx.get')
    def test_filter_by_area_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': None}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.meal_db.filter_by_area('NonExistentArea')
        self.assertIsInstance(response, MealList)

    @patch('httpx.get')
    def test_filter_by_area_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.filter_by_area('Canadian')

    @patch('httpx.get')
    def test_filter_by_area_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.filter_by_area('Canadian')

    # ─────────────────────────────────────────
    # get_latest_meal
    # ─────────────────────────────────────────
    @patch('httpx.get')
    def test_get_latest_meal_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Latest Meal'}]}
        mock_get.return_value = mock_response

        response = self.meal_db.get_latest_meal()
        self.assertIsInstance(response, (list, str))
        if isinstance(response, list):
            self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_get_latest_meal_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [1, 2, 3]}
        mock_get.return_value = mock_response

        response = self.meal_db.get_latest_meal()
        self.assertEqual(response, "You need to subscribe to The Meal DB API to access this endpoint")

    @patch('httpx.get')
    def test_get_latest_meal_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.get_latest_meal()

    @patch('httpx.get')
    def test_get_latest_meal_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Internal Server Error", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.get_latest_meal()

    # ─────────────────────────────────────────
    # get_ingredient_image
    # ─────────────────────────────────────────
    @patch('httpx.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_ingredient_image_success(self, mock_file, mock_get):
        mock_response = Mock()
        mock_response.content = b'fake_image_data'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.meal_db.get_ingredient_image('tomato')
        self.assertTrue(result)
        mock_file.assert_called_once_with('tomato.png', 'wb')

    @patch('httpx.get')
    def test_get_ingredient_image_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.get_ingredient_image('tomato')

    @patch('httpx.get')
    def test_get_ingredient_image_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "404 Not Found", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.get_ingredient_image('tomato')

    # ─────────────────────────────────────────
    # get_ingredient_image_small
    # ─────────────────────────────────────────
    @patch('httpx.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_ingredient_image_small_success(self, mock_file, mock_get):
        mock_response = Mock()
        mock_response.content = b'fake_image_data'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.meal_db.get_ingredient_image_small('tomato')
        self.assertTrue(result)
        mock_file.assert_called_once_with('tomato-small.png', 'wb')

    @patch('httpx.get')
    def test_get_ingredient_image_small_http_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")

        with self.assertRaises(httpx.HTTPError):
            self.meal_db.get_ingredient_image_small('tomato')

    @patch('httpx.get')
    def test_get_ingredient_image_small_status_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "404 Not Found", request=Mock(), response=Mock()
        )
        mock_get.return_value = mock_response

        with self.assertRaises(httpx.HTTPStatusError):
            self.meal_db.get_ingredient_image_small('tomato')


if __name__ == '__main__':
    unittest.main()