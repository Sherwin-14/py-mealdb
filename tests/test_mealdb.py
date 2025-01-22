import unittest
import httpx
import os

from unittest.mock import patch, Mock
from mealdb import MealDB 

class TestMealDB(unittest.TestCase):

     def setUp(self):
        self.api_key = 1
        self.meal_db = MealDB(self.api_key)

     def test_get_meal_by_name(self):
        name = 'Arrabiata'
        response = self.meal_db.get_meal_by_name(name)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_meal_details_by_id(self):
        id = 52772
        response = self.meal_db.meal_details_by_id(id)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_single_random_meal(self):
        response = self.meal_db.single_random_meal()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_list_all_meals(self):
        letter = 'a'
        response = self.meal_db.list_all_meals(letter)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_list_meal_categories(self):
        response = self.meal_db.list_meal_categories()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_list_all_categories(self):
        response = self.meal_db.list_all_categories()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_list_all_areas(self):
        response = self.meal_db.list_all_areas()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_list_all_ingredients(self):
        response = self.meal_db.list_all_ingredients()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_list_all(self):
        response = self.meal_db.list_all()
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_filter_by_ingredient(self):
        ingredient = 'Chicken'
        response = self.meal_db.filter_by_ingredient(ingredient)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_filter_by_category(self):
        category = 'Seafood'
        response = self.meal_db.filter_by_category(category)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_filter_by_area(self):
        area = 'Canadian'
        response = self.meal_db.filter_by_area(area)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

     def test_single_random_meal_error(self):
        with unittest.mock.patch('httpx.get') as mock_get:
            mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")
            with self.assertRaises(httpx.HTTPError):
                self.meal_db.single_random_meal()
     
     def test_get_latest_meal(self):
         response = self.meal_db.get_latest_meal()
         self.assertIsInstance(response, (list, str))
         if isinstance(response, list):
            self.assertGreater(len(response), 0)


     def test_get_latest_meal_subscription_required(self):
         with unittest.mock.patch('httpx.get') as mock_get:
            mock_data = {'meals': [1, 2, 3]}
            mock_get.return_value.json.return_value = mock_data
            response = self.meal_db.get_latest_meal()
            self.assertEqual(response, "You need to subscribe to The Meal DB API to access this endpoint")

     def test_get_latest_meal_error(self):
         with unittest.mock.patch('httpx.get') as mock_get:
            mock_get.side_effect = httpx.HTTPError("Mocked HTTP error")
            with self.assertRaises(httpx.HTTPError):
                  self.meal_db.get_latest_meal()

     def test_get_ingredient_image(self):
        result = self.meal_db.get_ingredient_image('tomato')
        self.assertEqual(result, "Fetched Image Successfully")

        # Check if the image was saved correctly
        self.assertTrue(os.path.exists('tomato.png'))

     def test_get_ingredient_image_small(self):
        result = self.meal_db.get_ingredient_image_small('tomato')
        self.assertEqual(result, "Fetched Image Successfully")

        # Check if the image was saved correctly
        self.assertTrue(os.path.exists('tomato-small.png'))

if __name__ == '__main__':
    unittest.main()
