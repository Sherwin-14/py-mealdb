import unittest
import unittest.mock
import httpx
import os

from py_mealdb import MealDB 
from unittest.mock import Mock, patch, mock_open


class TestMealDB(unittest.TestCase):

    def setUp(self):
        self.api_key = 1
        self.meal_db = MealDB(self.api_key)

    @patch('httpx.get')
    def test_get_meal_by_name(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Arrabiata'}]}
        mock_get.return_value = mock_response
        
        name = 'Arrabiata'
        response = self.meal_db.get_meal_by_name(name)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_meal_details_by_id(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Arrabiata'}]}
        mock_get.return_value = mock_response
        
        id = 52772
        response = self.meal_db.meal_details_by_id(id)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_single_random_meal(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Random Meal'}]}
        mock_get.return_value = mock_response
        
        response = self.meal_db.single_random_meal()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_list_all_meals(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Apple Pie'}]}
        mock_get.return_value = mock_response
        
        letter = 'a'
        response = self.meal_db.list_all_meals(letter)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_list_meal_categories(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'categories': [{'idCategory': '1', 'strCategory': 'Beef'}]}
        mock_get.return_value = mock_response
        
        response = self.meal_db.list_meal_categories()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_list_all_categories(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'categories': [{'strCategory': 'Beef'}, {'strCategory': 'Chicken'}]}
        mock_get.return_value = mock_response
        
        response = self.meal_db.list_all_categories()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_list_all_areas(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'strArea': 'American'}, {'strArea': 'British'}]}
        mock_get.return_value = mock_response
        
        response = self.meal_db.list_all_areas()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_list_all_ingredients(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idIngredient': '1', 'strIngredient': 'Chicken'}]}
        mock_get.return_value = mock_response
        
        response = self.meal_db.list_all_ingredients()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_list_all(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Meal 1'}]}
        mock_get.return_value = mock_response
        
        response = self.meal_db.list_all()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_filter_by_ingredient(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Chicken Curry'}]}
        mock_get.return_value = mock_response
        
        ingredient = 'Chicken'
        response = self.meal_db.filter_by_ingredient(ingredient)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_filter_by_category(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Salmon'}]}
        mock_get.return_value = mock_response
        
        category = 'Seafood'
        response = self.meal_db.filter_by_category(category)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_filter_by_area(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Poutine'}]}
        mock_get.return_value = mock_response
        
        area = 'Canadian'
        response = self.meal_db.filter_by_area(area)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_single_random_meal_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")
        with self.assertRaises(httpx.HTTPError):
            self.meal_db.single_random_meal()
    
    @patch('httpx.get')
    def test_get_latest_meal(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [{'idMeal': '52772', 'strMeal': 'Latest Meal'}]}
        mock_get.return_value = mock_response
        
        response = self.meal_db.get_latest_meal()
        self.assertIsInstance(response, (list, str))
        if isinstance(response, list):
            self.assertGreater(len(response), 0)

    @patch('httpx.get')
    def test_get_latest_meal_fail(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'meals': [1, 2, 3]}
        mock_get.return_value = mock_response
        
        response = self.meal_db.get_latest_meal()
        self.assertEqual(response, "You need to subscribe to The Meal DB API to access this endpoint")

    @patch('httpx.get')
    def test_get_latest_meal_error(self, mock_get):
        mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")
        with self.assertRaises(httpx.HTTPError):
            self.meal_db.get_latest_meal()

    @patch('httpx.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_ingredient_image(self, mock_file, mock_get):
        mock_response = Mock()
        mock_response.content = b'fake_image_data'
        mock_get.return_value = mock_response
        
        result = self.meal_db.get_ingredient_image('tomato')
        self.assertEqual(result, "Fetched Image Successfully")
        
        mock_file.assert_called_once_with('tomato.png', 'wb')

    @patch('httpx.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_ingredient_image_small(self, mock_file, mock_get):
        mock_response = Mock()
        mock_response.content = b'fake_image_data'
        mock_get.return_value = mock_response
        
        result = self.meal_db.get_ingredient_image_small('tomato')
        self.assertEqual(result, "Fetched Image Successfully")
        
        mock_file.assert_called_once_with('tomato-small.png', 'wb')


if __name__ == '__main__':
    unittest.main()
