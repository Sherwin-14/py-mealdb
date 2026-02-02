from py_mealdb import MealDB

mb = MealDB(1)
area = mb.list_all_categories()
# category = mb.list_all_areas()
# ingr = mb.list_all_ingredients()

print(area.categories)