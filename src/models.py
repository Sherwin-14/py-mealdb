from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Meals:
    strCategory: List[Dict[str, str]] = field(default_factory=list)
    strArea: List[Dict[str, str]] = field(default_factory=list)
    strIngredients: List[Dict[str, str]] = field(default_factory=list)

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
    def category(self) -> List[str]:
        """Get all meal IDs as a list."""
        return [meal['strCategory'] for meal in self.meals]
    
    @property
    def area(self) -> List[str]:
        """Get all meal names as a list."""
        return [meal['strArea'] for meal in self.meals]
    
    @property
    def ingredients(self) -> List[str]:
        """Get all thumbnail URLs as a list."""
        return [meal['strIngredients'] for meal in self.meals]



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