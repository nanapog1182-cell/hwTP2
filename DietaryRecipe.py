from Recipe import Recipe
from Ingredient import Ingredient

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None) -> None:
        self.diet_type = diet_type
        super().__init__(title, ingredients)

    def scale(self, ratio: float) -> 'DietaryRecipe':
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError(f"недопустимый коэффициент: {ratio!r}")
        new_ingredients = []
        for ing in self.ingredients:
            new_ingredients.append(Ingredient(ing.name, ing.quantity * ratio, ing.unit))
        return DietaryRecipe(self.title, self.diet_type, new_ingredients)

    def __str__(self) -> str:
        parent_str = super().__str__()
        return f"[{self.diet_type}] {parent_str}"