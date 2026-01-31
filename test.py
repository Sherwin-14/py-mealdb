from py_mealdb import MealDB

mb = MealDB(1)
meal = mb.meal_details_by_id('52772')

print(meal)