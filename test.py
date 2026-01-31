from py_mealdb import MealDB

mb = MealDB(1)
meal = mb.filter_by_ingredient('chicken_breast')

print(meal.names)