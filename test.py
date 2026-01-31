from py_mealdb import MealDB

mb = MealDB(1)
meal = mb.list_meal_categories()

print(meal.categories)