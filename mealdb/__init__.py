import httpx


def get_meal_by_name(name):

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
    data = r.json()
    meals = data['meals']
    
    return list(meals)


def list_all_meals(letter):

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}')
    data = r.json()
    meals = data['meals']
    
    return list(meals)


def meal_details_by_id(id):

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
    
    return r.json()


def single_random_meal():

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/random.php')
    
    return r.json()

def list_meal_categories():

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/categories.php')
    
    return r.json()







    