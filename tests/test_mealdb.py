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