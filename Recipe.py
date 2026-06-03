from Ingredient import Ingredient

class Recipe:
    def __init__(self, title: str, ingredients: list = None) -> None:
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []

    def add_ingredient(self, ingredient: Ingredient) -> None:
        for existing in self.ingredients:
            if existing.name == ingredient.name and existing.unit == ingredient.unit:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if isinstance(ratio, (int, float)) and ratio > 0:
            return True
        else:
            return False

    def scale(self, ratio: float) -> "Recipe":
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError(f"недопустимый коэффициент: {ratio!r}")
        new_recipe = Recipe(self.title)
        for ing in self.ingredients:
            new_recipe.ingredients.append(
                Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            )
        return new_recipe

    def __len__(self) -> int:
        return len(self.ingredients)

    def __str__(self) -> str:
        if not self.ingredients:
            return f"{self.title}: (ингредиенты не добавлены)"
        ingredients_str = "\n".join(f"  - {ing}" for ing in self.ingredients)
        return f"{self.title}:\n{ingredients_str}"