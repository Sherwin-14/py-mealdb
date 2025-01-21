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