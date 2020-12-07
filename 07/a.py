import re, pprint
pp = pprint.PrettyPrinter(indent=4)

def parseLine(line):
    line = line[:-1].split(' contain ')
    outer = line[0].split(' bags')[0]
    if 'no other bags' in line:
        return (outer, {})
    inner = line[1]
    inner = inner.split(', ')
    inner = map(lambda x: re.sub(' bag| bags', '', x), inner)
    inner_dict = {}
    for i in inner:
        split_inner = i.split()
        count = int(split_inner[0])
        color = ' '.join(split_inner[1:])
        if count > 1:
            color = color[:-1]
        inner_dict[color] = count
    return (outer, inner_dict)

def recursiveFindShinyGoldInBag(color_dict, contains_shiny_gold, bag_color):
    # print(bag_color)
    # print(color_dict)
    if not color_dict[bag_color]:
        return False
    if 'shiny gold' in color_dict[bag_color]:
        return True
    # print(bag_color, color_dict[bag_color], enumerate(color_dict[bag_color]))
    for color in color_dict[bag_color].keys():
        # print(color)
        if color in contains_shiny_gold:
            return True
        if recursiveFindShinyGoldInBag(color_dict, contains_shiny_gold, color):
            return True
    return False


def a(input):
    color_dict = {}
    contains_shiny_gold = set()
    for line in input:
        color, contains = parseLine(line)
        if color in color_dict:
            print("COLOR ALREADY DETECTED", color)
            return None
        color_dict[color] = contains
        if 'shiny gold' in contains:
            contains_shiny_gold.add(color)
    for color in color_dict:
        if color not in contains_shiny_gold and recursiveFindShinyGoldInBag(color_dict, contains_shiny_gold, color):
            contains_shiny_gold.add(color)

    pp.pprint(color_dict)
    pp.pprint(contains_shiny_gold)
    return len(contains_shiny_gold)
