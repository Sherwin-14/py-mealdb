from mealdb import Images as im


#meal_db = MealDB(1)  # Uses the default API key of '1'

# Get a meal by name
meal = im.get_small_ingredient_image('pork')
print(meal)