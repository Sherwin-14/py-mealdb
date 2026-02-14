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


Data models for TheMealDB API responses.

This module provides dataclass-based containers for various API response types,
including meals, categories, areas, and ingredients. All classes inherit from
BaseList which provides common functionality for list-based data structures.


"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Any, Generic, Union, Optional, Iterator

@dataclass
class BaseList:
    """
    Base class for list containers with common functionality.
    
    Provides standardized methods for working with list-based API responses,
    including iteration, indexing, length checking, and string representation.
    
    Attributes:
        items: List of dictionaries containing API response data.
    """
    items: List[Dict[str, Any]] = field(default_factory=list)
    
    @classmethod
    def from_response(cls, data: dict, key: str = 'meals') -> BaseList:
        """
        Create an instance from an API response dictionary.
        
        Args:
            data: The API response dictionary.
            key: The key to extract from the response. Defaults to 'meals'.
        
        Returns:
            An instance of the class with items populated from the response.
        """
        return cls(items=data.get(key, []))
    
    def __len__(self) -> int:
        """Return the number of items in the list."""
        return len(self.items)
    
    def __getitem__(self, index: int) -> Dict[str, Any]:
        """
        Get an item by index.
        
        Args:
            index: The index of the item to retrieve.
        
        Returns:
            The item at the specified index.
        """
        return self.items[index]
    
    def __iter__(self) -> Iterator[Dict[str, Any]]:
        """Return an iterator over the items."""
        return iter(self.items)
    
    def __repr__(self) -> str:
        """Return a string representation showing the class name and item count."""
        return f"{self.__class__.__name__}(count={len(self.items)})"


@dataclass
class MealList(BaseList):
    """
    Container for meal summary data.
    
    Used for endpoints that return basic meal information including
    meal ID, name, and thumbnail. Typically used for filter and list endpoints.
    """
    
    @property
    def ids(self) -> List[str]:
        """
        Get all meal IDs from the list.
        
        Returns:
            List of meal IDs.
        """
        return [meal['idMeal'] for meal in self.items]
    
    @property
    def names(self) -> List[str]:
        """
        Get all meal names from the list.
        
        Returns:
            List of meal names.
        """
        return [meal['strMeal'] for meal in self.items]
    
    @property
    def thumbnails(self) -> List[str]:
        """
        Get all meal thumbnail URLs from the list.
        
        Returns:
            List of thumbnail URLs.
        """
        return [meal['strMealThumb'] for meal in self.items]


@dataclass
class AreaList(BaseList):
    """
    Container for area/region data.
    
    Used for endpoints that return geographical areas or cuisines available
    in TheMealDB.
    """
    
    @property
    def areas(self) -> List[str]:
        """
        Get all area names from the list.
        
        Returns:
            List of area names.
        """
        return [item['strArea'] for item in self.items]


@dataclass
class CategoryList(BaseList):
    """
    Container for meal category data.
    
    Used for endpoints that return meal categories available in TheMealDB.
    """
    
    @property
    def categories(self) -> List[str]:
        """
        Get all category names from the list.
        
        Returns:
            List of category names.
        """
        return [item['strCategory'] for item in self.items]


@dataclass
class IngredientList(BaseList):
    """
    Container for ingredient data.
    
    Used for endpoints that return available ingredients in TheMealDB.
    """
    
    @property
    def ingredients(self) -> List[str]:
        """
        Get all ingredient names from the list.
        
        Returns:
            List of ingredient names.
        """
        return [item['strIngredient'] for item in self.items]


@dataclass
class MealDetails(BaseList):
    """
    Container for detailed meal information.
    
    Used for endpoints that return complete meal data including instructions,
    ingredients, measurements, tags, and other detailed information.
    """
    
    @classmethod
    def from_response(cls, data: dict, key: str = 'meals') -> MealDetails:
        """
        Create an instance from an API response, handling null meal data.
        
        Args:
            data: The API response dictionary.
            key: The key to extract from the response. Defaults to 'meals'.
        
        Returns:
            Instance with meals populated, or empty list if meals is None.
        """
        meals_data = data.get(key)
        if meals_data is None:
           return cls(items=[])
        return cls(items=meals_data)
    
    @property
    def ids(self) -> List[str]:
        """
        Get all meal IDs from the list.
        
        Returns:
            List of meal IDs.
        """
        return [meal['idMeal'] for meal in self.items]
    
    @property
    def names(self) -> List[str]:
        """
        Get all meal names from the list.
        
        Returns:
            List of meal names.
        """
        return [meal['strMeal'] for meal in self.items]
    
    @property
    def categories(self) -> List[str]:
        """
        Get all meal categories from the list.
        
        Returns:
            List of meal categories.
        """
        return [meal['strCategory'] for meal in self.items]
    
    @property
    def areas(self) -> List[str]:
        """
        Get all meal areas/cuisines from the list.
        
        Returns:
            List of meal areas.
        """
        return [meal['strArea'] for meal in self.items]
    
    def get_ingredients(self, meal_index: int = 0) -> List[Dict[str, str]]:
        """
        Extract ingredients and measurements from a specific meal.
        
        Args:
            meal_index: Index of the meal to extract ingredients from. Defaults to 0.
        
        Returns:
            List of ingredient dictionaries with 'name' and 'measure' keys.
            Empty list if index is invalid.
        """
        if meal_index >= len(self.items):
            return []
        
        meal = self.items[meal_index]
        ingredients = []
        
        for i in range(1, 21):
            ingredient_name = meal.get(f'strIngredient{i}')
            measure = meal.get(f'strMeasure{i}')
            
            if ingredient_name and ingredient_name.strip():
                ingredients.append({
                    'name': ingredient_name.strip(),
                    'measure': measure.strip() if measure else ""
                })
        
        return ingredients
    
    def get_tags(self, meal_index: int = 0) -> List[str]:
        """
        Extract tags from a specific meal.
        
        Args:
            meal_index: Index of the meal to extract tags from. Defaults to 0.
        
        Returns:
            List of tag strings. Empty list if no tags or invalid index.
        """
        if meal_index >= len(self.items):
            return []
        
        meal = self.items[meal_index]
        tags_str = meal.get('strTags')
        
        if tags_str:
            return [tag.strip() for tag in tags_str.split(',')]
        return []