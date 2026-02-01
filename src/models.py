from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Meals:
    Category: List[Dict[str, str]] = field(default_factory=list)
    Area: List[Dict[str, str]] = field(default_factory=list)
    Ingredients: List[Dict[str, str]] = field(default_factory=list)

    @classmethod
    def from_area(cls, data: dict) -> Meals:
        """Create from API response like {'meals': [...]}"""
        return cls(Area= data.get("meals",[]))

    @classmethod
    def from_categories(cls, data: dict) -> Meals:
        """Create from API response like {'meals': [...]}"""
        return cls(Category= data.get("meals",[]))

    @classmethod
    def from_ingredients(cls, data: dict) -> Meals:
        """Create from API response like {'meals': [...]}"""
        return cls(Ingredients= data.get("meals",[]))

    def _active_list(self) -> List[Dict[str, str]]:
        """Returns whichever list is currently populated."""
        if self.Area:
            return self.Area
        elif self.Category:
            return self.Category
        elif self.Ingredients:
            return self.Ingredients
        return []

    def __len__(self) -> int:
        return len(self._active_list())

    def __getitem__(self, index: int) -> Dict[str, str]:
        return self._active_list()[index]

    def __iter__(self):
        return iter(self._active_list())

    def __repr__(self) -> str:
        return f"Meals(count={len(self)})"

    @property
    def area(self) -> List[str]:
        """Get all meal names as a list."""
        return [meal['strArea'] for meal in self.Area]

    @property
    def category(self) -> List[str]:
        """Get all meal names as a list."""
        return [meal['strCategory'] for meal in self.Category]

    @property
    def ingredients(self) -> List[str]:
        """Get all meal names as a list."""
        return [meal['strIngredient'] for meal in self.Ingredients]


@dataclass
class MealList:
    """Container for multiple meals with convenient access methods."""
    meals: List[Dict[str, Any]] = field(default_factory=list)
    
    @classmethod
    def from_response(cls, data: dict) -> 'MealList':
        """Create from API response like {'meals': [...]}"""
        return cls(meals=data.get('meals', []))
    
    def __len__(self) -> int:
        return len(self.meals)
    
    def __getitem__(self, index: int) -> Dict[str, Any]:
        return self.meals[index]
    
    def __iter__(self):
        return iter(self.meals)
    
    def __repr__(self) -> str:
        return f"MealList(count={len(self.meals)})"
    
    @property
    def ids(self) -> List[str]:
        """Get all meal IDs as a list."""
        return [meal['idMeal'] for meal in self.meals]
    
    @property
    def names(self) -> List[str]:
        """Get all meal names as a list."""
        return [meal['strMeal'] for meal in self.meals]
    
    @property
    def thumbnails(self) -> List[str]:
        """Get all thumbnail URLs as a list."""
        return [meal['strMealThumb'] for meal in self.meals]