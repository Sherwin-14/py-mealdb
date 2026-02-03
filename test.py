from py_mealdb import MealDB

mb = MealDB(1)
area = mb.get_meal_by_name('Arrabiata')
# category = mb.list_all_areas()
# ingr = mb.list_all_ingredients()

print(area.names)