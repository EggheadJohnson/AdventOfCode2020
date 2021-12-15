import pprint, functools
pp = pprint.PrettyPrinter(indent=4)

def prepLine(line):
    split_line = line.split(' (contains ')
    alien_ingredients = split_line[0].split(' ')
    known_allergens = split_line[1][:-1].split(', ')
    return alien_ingredients, known_allergens

def makeIngredientCounts(parsed_input):
    ingredient_counts = {}
    for ingredients, allergens in parsed_input:
        for ingredient in ingredients:
            if ingredient not in ingredient_counts:
                ingredient_counts[ingredient] = {}
            for allergen in allergens:
                ingredient_counts[ingredient][allergen] = ingredient_counts[ingredient].get(allergen, 0) + 1
    return ingredient_counts

def getHighestMatchSet(allergen_counts):
    highest_match_set = set()
    highest_seen = 0
    for key, val in allergen_counts.items():
        if val > highest_seen:
            highest_seen = val
            highest_match_set = set()
        if val == highest_seen:
            highest_match_set.add(key)
    return highest_match_set

def makeHighestMatchSets(ingredient_counts):
    highest_match_sets = {}
    for key, val_dict in ingredient_counts.items():
        highest_match_sets[key] = getHighestMatchSet(val_dict)
    return highest_match_sets

def makeAllergenCounts(parsed_input):
    allergenCounts = {}
    for ingredients, allergens in parsed_input:
        for allergen in allergens:
            if allergen not in allergenCounts:
                allergenCounts[allergen] = {}
            for ingredient in ingredients:
                allergenCounts[allergen][ingredient] = allergenCounts[allergen].get(ingredient, 0) + 1
    return allergenCounts

def makeAllergenSets(parsedInput):
    allergenSets = {}
    for ingredients, allergens in parsedInput:
        for allergen in allergens:
            if allergen not in allergenSets:
                allergenSets[allergen] = set(ingredients)
            else:
                allergenSets[allergen] = allergenSets[allergen] & set(ingredients)
    return allergenSets

def buildFullIngredientSet(parsedInput):
    ingredientSet = set()
    for ingredients, _ in parsedInput:
        ingredientSet = ingredientSet | set(ingredients)
    return ingredientSet

def buildSuspectedAllergens(allergenSets):
    suspectedAllergens = set()
    for allergenSet in allergenSets.values():
        suspectedAllergens = suspectedAllergens | allergenSet
    return suspectedAllergens

def getUsageCount(safeIngredients, parsedInput):
    total = 0
    return sum([ sum([ 1 if ingredient in safeIngredients else 0 for ingredient in line[0] ]) for line in parsedInput ])

def a(input):
    parsedInput = list(map(prepLine, input))
    # pp.pprint(parsedInput)
    ingredientSet = buildFullIngredientSet(parsedInput)
    # pp.pprint(ingredientSet)
    allergenSets = makeAllergenSets(parsedInput)
    # pp.pprint(allergenSets)
    suspectedAllergens = buildSuspectedAllergens(allergenSets)
    # pp.pprint(suspectedAllergens)
    safeIngredients = ingredientSet - suspectedAllergens
    # pp.pprint(safeIngredients)
    return getUsageCount(safeIngredients, parsedInput)
