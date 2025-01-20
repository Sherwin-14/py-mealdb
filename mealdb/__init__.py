import httpx

def get_meal_by_name(name) -> list:  
    """
    Retrieves a list of meals by name from the MealDB API.

    Args:
        name (str): The name of the meal to search for. (e.g. Arrabiata, Potato Salad, Blini Pancakes).

    Returns:
        list: A list of meals matching the search query.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to search for meals by name.
        The API returns a list of meals, which is then returned by this function.
    """
    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
    data = r.json()
    meal = data['meals']
    return list(meal)


def list_all_meals(letter) -> list:
    """
    Retrieves a list of meals starting with a specific letter from the MealDB API.

    Args:
        letter (str): The letter to search for (e.g. 'a', 'b', etc.).

    Returns:
        list: A list of meals starting with the specified letter.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to search for meals by letter.
        The API returns a list of meals, which is then returned by this function.
    """
    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}')
    data = r.json()
    meals = data['meals']
    
    return list(meals)


def meal_details_by_id(id) -> list:
    """
    Retrieves the details of a meal by its ID from the MealDB API.

    Args:
        id (int): The ID of the meal to retrieve. (e.g. 52772).

    Returns:
        list: A list containing the details of the meal.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve the details of a meal by its ID.
        The API returns a list containing the meal details, which is then returned by this function.
    """
    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
    data = r.json()
    meal = data['meals']
    
    return list(meal)


def single_random_meal() -> list:
    """
    Retrieves a single random meal from the MealDB API.

    Returns:
        list: A list containing the details of a random meal.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve a single random meal.
        The API returns a list containing the meal details, which is then returned by this function.
    """
    r = httpx.get('https://www.themealdb.com/api/json/v1/1/random.php')
    data = r.json()
    meal = data['meals']
    
    return list(meal)

def list_meal_categories() -> list:
    """
    Retrieves a list of meal categories from the MealDB API.

    Returns:
        dict: A dictionary containing the list of meal categories.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve a list of meal categories.
        The API returns a dictionary containing the categories, which is then returned by this function.
    """
    r = httpx.get('https://www.themealdb.com/api/json/v1/1/categories.php')
    data = r.json()
    meal = data['meals']
    
    return r.json()

def list_all_categories() -> list:
    """
    Retrieves a list of all categories from the MealDB API.

    Returns:
        list: A list of dictionaries containing the categories.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve a list of all categories.
        The API returns a dictionary containing the categories, which is then converted to a list and returned by this function.
    """
    r = httpx.get('https://www.themealdb.com/api/json/v1/1/categories.php')
    data = r.json()
    
    return list(data)

def list_all_areas() -> list:
    """
    Retrieves a list of all areas from the MealDB API.

    Returns:
        list: A list of dictionaries containing the areas.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve a list of all areas.
        The API returns a dictionary containing the areas, which is then converted to a list and returned by this function.
    """
    r = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
    data = r.json()
    areas = data['meals']
    
    return list(areas)

def list_all_ingredients() -> list:
    """
    Retrieves a list of all ingredients from the MealDB API.

    Returns:
        list: A list of dictionaries containing the ingredients.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve a list of all ingredients.
        The API returns a dictionary containing the ingredients, which is then converted to a list and returned by this function.
    """
    r = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
    data = r.json()
    ingredients = data['meals']
    
    return list(ingredients)

def list_all() -> list:
    """
    Retrieves a list of all categories, areas, and ingredients from the MealDB API.

    Returns:
        list: A list of dictionaries containing the categories, areas, and ingredients.

    Raises:
        httpx.HTTPError: If any of the API requests fail.

    Notes:
        This function uses the MealDB API to retrieve a list of all categories, areas, and ingredients.
        The API returns a dictionary containing the categories, areas, and ingredients, which are then combined into a list and returned by this function.
    """
    r1 = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
    data1 = r1.json()

    r2 = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
    data2 = r2.json()

    r3 = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
    data3 = r3.json()

    answers = [data1, data2, data3]

    return answers

def filter_by_ingredient(ingredient) -> list:
    """
    Retrieves a list of meals that include a specific ingredient from the MealDB API.

    Args:
        ingredient (str): The ingredient to filter by (e.g. Chicken, Salmon, Beef).

    Returns:
        list: A list of dictionaries containing the meals that include the specified ingredient.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve a list of meals that include a specific ingredient.
        The API returns a dictionary containing the meals, which is then converted to a list and returned by this function.
    """
    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}')
    data = r.json()
    meal = data['meals']
    
    return list(meal)

def filter_by_category(category) -> list:
    """
    Retrieves a list of meals that belong to a specific category from the MealDB API.

    Args:
        category (str): The category to filter by.

    Returns:
        list: A list of dictionaries containing the meals that belong to the specified category.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve a list of meals that belong to a specific category.
        The API returns a dictionary containing the meals, which is then converted to a list and returned by this function.
    """
    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}')
    data = r.json()
    meal = data['meals']
    
    return list(meal)

def filter_by_area(area) -> list:
    """
    Retrieves a list of meals that originate from a specific area from the MealDB API.

    Args:
        area (str): The area to filter by (e.g. Canadian, Mexican).

    Returns:
        list: A list of dictionaries containing the meals that originate from the specified area.

    Raises:
        httpx.HTTPError: If the API request fails.

    Notes:
        This function uses the MealDB API to retrieve a list of meals that originate from a specific area.
        The API returns a dictionary containing the meals, which is then converted to a list and returned by this function.
    """
    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={area}')
    data = r.json()
    meal = data['meals']
    
    return list(meal)