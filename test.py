from mealdb import MealDB


#meal_db = MealDB(1)  # Uses the default API key of '1'
mb = MealDB(1)
# Get a meal by name
meal = mb.get_ingredient_image_small('pork')
print(meal)