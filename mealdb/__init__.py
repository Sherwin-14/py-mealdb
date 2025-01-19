import httpx


def get_meal_by_name(name):  

    r = httpx.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
    data = r.json()
    meal = data['meals']
    return list(meal)


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









    