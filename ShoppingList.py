from Ingredient import Ingredient
from Recipe import Recipe

class ShoppingList:
    def __init__(self) -> None:
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if not Recipe.is_valid_ratio(portions):
            raise ValueError("Количество порций должно быть положительным числом")
        scaled_recipe = recipe.scale(portions)
        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str) -> None:
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self) -> list:
        aggregated = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in aggregated:
                aggregated[key] += ingredient.quantity
            else:
                aggregated[key] = ingredient.quantity
        result = []
        for (name, unit), quantity in aggregated.items():
            result.append(Ingredient(name, quantity, unit))
        result.sort(key=lambda x: x.name)
        return result

    def __add__(self, other: 'ShoppingList') -> 'ShoppingList':
        if not isinstance(other, ShoppingList):
            raise TypeError("можно объединять только ShoppingList с ShoppingList")
        new_list = ShoppingList()
        new_list._items = self._items.copy() + other._items.copy()
        return new_list