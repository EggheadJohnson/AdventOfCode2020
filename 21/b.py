from a import *

def figureItOut(allergenSets):
    knownIngredients = set()
    knownAllergens = set()
    changesMade = True
    while changesMade:
        changesMade = False
        for allergen, ingredients in allergenSets.items():
            if allergen in knownAllergens:
                continue
            if len(ingredients) == 1:
                ingredient = next(iter(ingredients))
                for key in allergenSets:

                    if key != allergen and ingredient in allergenSets[key]:
                        allergenSets[key].remove(ingredient)
                knownIngredients.add(ingredient)
                knownAllergens.add(allergen)
                changesMade = True
    return allergenSets

def b(input):
    parsedInput = list(map(prepLine, input))
    # pp.pprint(parsedInput)
    ingredientSet = buildFullIngredientSet(parsedInput)
    # pp.pprint(ingredientSet)
    allergenSets = makeAllergenSets(parsedInput)
    pp.pprint(allergenSets)
    # suspectedAllergens = buildSuspectedAllergens(allergenSets)
    # pp.pprint(suspectedAllergens)
    # safeIngredients = ingredientSet - suspectedAllergens
    # pp.pprint(safeIngredients)
    allergenSets = figureItOut(allergenSets)
    pp.pprint(allergenSets)
    allergens = list(map(lambda a: next(iter(allergenSets[a])), sorted(allergenSets.keys())))
    pp.pprint(allergens)

    return ','.join(allergens)
