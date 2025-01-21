import unittest
import httpx
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
        self.assertIsInstance(response, dict)
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
            mock_get.side_effect = httpx.HTTPError
            with self.assertRaises(httpx.HTTPError):
                self.meal_db.single_random_meal()

if __name__ == '__main__':
    unittest.main()
