from mealdb import MealDB


meal_db = MealDB(1)  # Uses the default API key of '1'

# Get a meal by name
meal = meal_db.get_ingredient_image('pork')
print(meal)