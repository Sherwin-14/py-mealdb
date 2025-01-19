import httpx


def get_meal_by_name(name):  
    try:
        r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
        data = r.json()
        meal = data['meals']
        return list(meal)
    
    except httpx.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except httpx.ConnectTimeout as conn_err:
        print(f'Connection timeout error occurred: {conn_err}')

    except httpx.TimeoutException as time_err:
        print(f'An operation has timed out: {time_err}')

    except httpx.ReadTimeout as redtime_err:
        print(f'Timed out while receiving data from the host: {redtime_err}')

    except httpx.ConnectError as conn_err:
        print(f'Failed to establish a connection: {conn_err}')

    except httpx.ReadError as read_err:
        print(f'Failed to receive data from the network: {read_err}')


def list_all_meals(letter):

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}')
    data = r.json()
    meals = data['meals']
    
    return list(meals)


def meal_details_by_id(id):

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
    data = r.json()
    meal = data['meals']
    
    return list(meal)


def single_random_meal():

    r = httpx.get('https://www.themealdb.com/api/json/v1/1/random.php')
    data = r.json()
    meal = data['meals']
    
    return list(meal)

def list_meal_categories():

    r = httpx.get('https://www.themealdb.com/api/json/v1/1/categories.php')
    
    return r.json()

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









    