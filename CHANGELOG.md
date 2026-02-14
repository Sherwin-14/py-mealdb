# Changelog

## [1.0.0] - 2026-02-14

### Breaking Changes
- All methods now return typed objects instead of raw lists:
  - `get_meal_by_name()` → `MealDetails`
  - `meal_details_by_id()` → `MealDetails`
  - `single_random_meal()` → `MealDetails`
  - `list_all_meals()` → `MealDetails`
  - `list_meal_categories()` → `CategoryList`
  - `list_all_categories()` → `CategoryList`
  - `list_all_areas()` → `AreaList`
  - `list_all_ingredients()` → `IngredientList`
  - `filter_by_ingredient()` → `MealList`
  - `filter_by_category()` → `MealList`
  - `filter_by_area()` → `MealList`
  - `list_all()` → `Dict[str, Union[CategoryList, AreaList, IngredientList]]`
  - `get_ingredient_image()` → `bool`
  - `get_ingredient_image_small()` → `bool`

### Migration Guide
If you were accessing data like this before:
\```python
# v0.1.8 (old)
meals = mb.get_meal_by_name('Arrabiata')
for meal in meals:
    print(meal['strMeal'])
\```

Update to this:
\```python
# v1.0 (new)
meals = mb.get_meal_by_name('Arrabiata')

# Option 1: Use convenience properties
print(meals.names)

# Option 2: Still works with indexing
for meal in meals:
    print(meal['strMeal'])

# Option 3: Access single meal
print(meals[0]['strMeal'])
\```

### Added
- New data models in `models.py`:
  - `BaseList` - Base class for all list containers
  - `MealDetails` - Detailed meal information
  - `MealList` - Simplified meal summaries
  - `CategoryList` - Category data with `.categories` property
  - `AreaList` - Area data with `.areas` property
  - `IngredientList` - Ingredient data with `.ingredients` property
- Convenience properties on all model classes (`.names`, `.ids`, `.areas`, etc.)
- Proper type hints across all methods

### Fixed
- `raise_for_status()` now consistently called across all methods
- Empty response handling (`None` meals) handled gracefully