from py_mealdb import MealDB

mb = MealDB(1)
meal = mb.list_all_areas()

print(meal.area)