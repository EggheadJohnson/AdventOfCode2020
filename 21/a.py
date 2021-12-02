import pprint
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

def a(input):
    parsed_input = list(map(prepLine, input))
    print(parsed_input)
    ingredient_counts = makeIngredientCounts(parsed_input)
    pp.pprint(ingredient_counts)
    highest_match_sets = makeHighestMatchSets(ingredient_counts)
    pp.pprint(highest_match_sets)
    return None
