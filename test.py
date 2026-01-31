from py_mealdb import MealDB

mb = MealDB(1)
meal = mb.filter_by_area('Canadian')

print(meal.__getitem__(2))