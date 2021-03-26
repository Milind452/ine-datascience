def test_ingredients():
    assert type(pizza_ingredients) == list, "Should be a List"
    assert len(pizza_ingredients) == 5, "Should have 5 ingredients"
    assert type(ingredient_4) == str, "Should be a String"
    assert ingredient_4 == pizza_ingredients[3], "Should be equal to the 4th ingredient"

if __name__ == "__main__":
    pizza_ingredients = None
    ingredient_4 = None


    pizza_ingredients = ['cheese', 'pepper', 'onion', 'chicken', 'tomato']
    ingredient_4 = pizza_ingredients[3]