from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime

@dataclass
class Meal:
    idMeal: str
    strMeal: str
    strCategory: str
    strArea: str
    strInstructions: str
    strMealThumb: str
    strYoutube: str

    # Optional fields
    strMealAlternate: Optional[str] = None
    strTags: Optional[str] = None
    strSource: Optional[str] = None
    strImageSource: Optional[str] = None
    strCreativeCommonsConfirmed: Optional[str] = None
    dateModified: Optional[str] = None
    
    strIngredients: list[Optional[str]]
    strMeasure: list[Optional[str]]

    








    