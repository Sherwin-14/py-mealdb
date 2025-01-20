import httpx

def get_meal_by_name(name):  
    """
    Retrieves a list of meals by name from the MealDB API.

    Args:
        name (str): The name of the meal to search for.

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


def list_all_meals(letter):
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


def meal_details_by_id(id):
    """
    Retrieves the details of a meal by its ID from the MealDB API.

    Args:
        id (int): The ID of the meal to retrieve.

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


def single_random_meal():
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

def list_meal_categories():
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

def list_all_categories():
    
    r = httpx.get('https://www.themealdb.com/api/json/v1/1/categories.php')
    data = r.json()
    
    return list(data)

def list_all_areas():
    
    r = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
    data = r.json()
    areas = data['meals']
    
    return list(areas)

def list_all_ingredients():
    
    r = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
    data = r.json()
    ingredients = data['meals']
    
    return list(ingredients)

def list_all():
    
     r1 = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
     data1 = r1.json()

     r2 = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
     data2 = r2.json()

     r3 = httpx.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
     data3 = r3.json()

     answers = [data1, data2, data3]

     return answers

def filter_by_ingredient(ingredient):

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}')
    data = r.json()
    meal = data['meals']
    
    return list(meal)

def filter_by_category(category):

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}')
    data = r.json()
    meal = data['meals']
    
    return list(meal)

def filter_by_area(area):

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={area}')
    data = r.json()
    meal = data['meals']
    
    return list(meal)