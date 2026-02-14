"""
*********************************************************************
* Copyright (c) 2026 Sherwin Varghese
* This program and the accompanying materials are made
* available under the terms of the Eclipse Public License 2.0
* which is available at https://www.eclipse.org/legal/epl-2.0/
*
*
* SPDX-License-Identifier: EPL-2.0
**********************************************************************


Python client for TheMealDB API.

This module provides a simple interface to interact with TheMealDB API endpoints.

"""

import httpx

from .models import (
    BaseList,
    MealList,
    MealDetails,
    AreaList,
    CategoryList,
    IngredientList
)

class MealDB:
    """
    Client for interacting with TheMealDB API.
    
    Attributes:
        api_key: The API key for authentication.
        base_url: The base URL for API requests.
    """

    def __init__(self, api_key):
      """
      Initialize the MealDB client.
    
      Args:
        api_key: API key for TheMealDB. Use '1' for testing.
      """
      self.api_key = api_key
      self.base_url = f'https://www.themealdb.com/api/json/v1/{api_key}'

    def get_meal_by_name(self,name:str) -> MealDetails:  
        """
        Retrieves detailed meal information by searching for a meal name.

        Args:
            name: The name of the meal to search for (e.g., 'Arrabiata', 'Potato Salad').

        Returns:
            MealDetails object containing detailed meal information.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/search.php?s={name}')
        r.raise_for_status()
        return MealDetails.from_response(r.json())
    
    def get_latest_meal(self) -> Union[str, list]:
        """
        Retrieves the latest meal data from the API.

        Returns:
            String message if subscription is required, otherwise MealDetails object containing the latest meal data.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.

        Note:
            This endpoint requires a subscription to The MealDB API. Without a subscription,
            a message is returned instead of meal data.
        """
        r = httpx.get(f'{self.base_url}/latest.php')
        r.raise_for_status()
        data = r.json()
        meal = data['meals']
        if len(meal) == 3:
            return "You need to subscribe to The Meal DB API to access this endpoint"
        else:
            return list(meal)
           
    def meal_details_by_id(self,id:str) -> MealDetails:
        """
        Retrieves detailed meal information by meal ID.

        Args:
            id: The meal ID to retrieve (e.g., '52772').

        Returns:
            MealDetails object containing the meal's complete information.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/lookup.php?i={id}')
        r.raise_for_status()
        return MealDetails.from_response(r.json())

    def single_random_meal(self) -> MealDetails:
        """
        Retrieves a single random meal from the MealDB API.

        Returns:
            MealDetails object containing a random meal's complete information.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/random.php')
        r.raise_for_status()
        return MealDetails.from_response(r.json())

    def list_all_meals(self,letter:str) -> MealDetails:
        """
        Retrieves meals starting with a specific letter.

        Args:
            letter: The first letter to search for (e.g., 'a', 'b', 'c').

        Returns:
            MealDetails object containing all meals starting with the specified letter.

        Raises:
            httpx.HTTPError:Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/search.php?f={letter}')
        r.raise_for_status()
        return MealDetails.from_response(r.json())

    def list_meal_categories(self) -> CategoryList:
        """
        Retrieves detailed information about all meal categories.

        Returns:
            CategoryList object containing detailed category information including descriptions and thumbnails.

        Raises:
            httpx.HTTPError:Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/categories.php')
        r.raise_for_status()
        return CategoryList.from_response(r.json(), key = "categories")

    def list_all_categories(self) -> CategoryList:
        """
        Retrieves a simple list of all category names.

        Returns:
            CategoryList object containing category names.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/categories.php')
        r.raise_for_status()
        return CategoryList.from_response(r.json(), key='categories')

    def list_all_areas(self) -> AreaList:
        """
        Retrieves all available geographical areas/cuisines.

        Returns:
            AreaList object containing all available area names.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/list.php?a=list')
        r.raise_for_status()
        return AreaList.from_response(r.json())

    def list_all_ingredients(self) -> IngredientList:
        """
        Retrieves all available ingredients.

        Returns:
            IngredientList object containing all available ingredient names.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/list.php?i=list')
        r.raise_for_status()
        return IngredientList.from_response(r.json())

    def list_all(self) -> Dict[str, Union[CategoryList, AreaList, IngredientList]]:
        """
        Retrieves all categories, areas, and ingredients in a single call.

        Returns:
            Dictionary with keys 'categories', 'areas', and 'ingredients' containing their respective list objects.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r1 = httpx.get(f'{self.base_url}/list.php?c=list')
        r1.raise_for_status()
        
        r2 = httpx.get(f'{self.base_url}/list.php?a=list')
        r2.raise_for_status()

        r3 = httpx.get(f'{self.base_url}/list.php?i=list')
        r3.raise_for_status()

        return {
        'categories': CategoryList.from_response(r1.json(), key='categories'),
        'areas': AreaList.from_response(r2.json()),
        'ingredients': IngredientList.from_response(r3.json())
        }

    def filter_by_ingredient(self,ingredient:str) -> MealList:
        """
        Retrieves meals containing a specific ingredient.

        Args:
            ingredient: The ingredient to filter by (e.g., 'Chicken', 'Salmon', 'Beef').

        Returns:
            MealList object containing meal summaries that include the specified ingredient.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/filter.php?i={ingredient}')
        r.raise_for_status()
        return MealList.from_response(r.json())
    
    def filter_by_category(self,category:str) -> MealList:
        """
        Retrieves meals belonging to a specific category.

        Args:
            category: The category to filter by (e.g., 'Seafood', 'Dessert', 'Vegetarian').

        Returns:
            MealList object containing meal summaries from the specified category.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/filter.php?c={category}')
        r.raise_for_status()
        return MealList.from_response(r.json())

    def filter_by_area(self,area:str) -> MealList:
        """
        Retrieves meals from a specific geographical area/cuisine.

        Args:
            area: The area to filter by (e.g., 'Canadian', 'Mexican', 'Italian').

        Returns:
            MealList object containing meal summaries from the specified area.

        Raises:
            httpx.HTTPError: Check httpx's documentation for all possible exceptions.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r = httpx.get(f'{self.base_url}/filter.php?a={area}')
        r.raise_for_status()
        return MealList.from_response(r.json())
    
    def get_ingredient_image(self,ingredient:str) -> bool:
        """
        Fetches and saves a full-size ingredient image locally.

        Args:
            ingredient: The ingredient name (e.g., 'tomato', 'chicken').

        Returns:
            True if the image was successfully fetched and saved, False otherwise.

        Raises:
            httpx.HTTPError: If the HTTP request fails.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r =  httpx.get(f'https://www.themealdb.com/images/ingredients/{ingredient}.png')
        r.raise_for_status()
        image_data = r.content
        with open(f'{ingredient}.png', 'wb') as file:
            file.write(image_data)
            return True
    
        return False
        
    def get_ingredient_image_small(self,ingredient:str) -> bool:
        """
        Fetches and saves a small-size ingredient image locally.

        Args:
            ingredient: The ingredient name (e.g., 'tomato', 'chicken').

        Returns:
            True if the image was successfully fetched and saved, False otherwise.

        Raises:
            httpx.HTTPError: If the HTTP request fails.
            httpx.HTTPStatusError: If the API returns a non-2xx status code.
        """
        r =  httpx.get( f'https://www.themealdb.com/images/ingredients/{ingredient}-Small.png')
        r.raise_for_status()
        image_data = r.content
        with open(f'{ingredient}-small.png', 'wb') as file:
            file.write(image_data)
            return True
    
        return False
    