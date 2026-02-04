from py_mealdb import MealDB

mb = MealDB(1)
all_data = mb.single_random_meal()
# category = mb.list_all_areas()
# ingr = mb.list_all_ingredients()

print(all_data.names)