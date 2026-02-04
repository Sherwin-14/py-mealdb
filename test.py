from py_mealdb import MealDB

mb = MealDB(1)
all_data = mb.list_all()
# category = mb.list_all_areas()
# ingr = mb.list_all_ingredients()

print(all_data['areas'].areas)