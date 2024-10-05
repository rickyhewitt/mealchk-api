# mealchk-cli
# mealchk.py
# ricky@rickyhewitt.dev

import re

# Load list of prohibited ingredients
with open("ingredients.txt") as f:
    prohibitedList = f.read().splitlines() 


def analyze(ingredientsRaw):
    # Create variables
    passFlag = True
    ingredientList = []
    detectedList = []
    passedList = []
    failedList = []

    # Split input by comma seperation, while ignoring anything in brackets
    # regex = "/,(?![^(]*\)) /;"
    ingredients = ingredientsRaw.lstrip().lower().replace("ingredients", "")
    ingredients = re.split(r",(?![^(]*\))", ingredients)

    # # Trim each ingredient further
    for i in ingredients:
        formattedIngredient = i.strip().replace("\n", " ").replace(".", "")
        formattedIngredient = formattedIngredient.strip()
        # Append (if not duplicate)
        if formattedIngredient not in ingredientList:
            ingredientList.append(formattedIngredient)

    print("Ingredients list: \n", ingredientList)

    for ingredient in ingredientList:
        # print("Ingredient: ", ingredient)
        for prohibited in prohibitedList:
            if ingredient.find(prohibited) > 0 or ingredient == prohibited:
                # print("Found: ", (ingredient))
                detectedList.append(ingredient)
                # print("Found: ", ingredient)

    print("\n", "Warning: ", detectedList)