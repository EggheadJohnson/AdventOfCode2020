from a import parseLine
import pprint
pp = pprint.PrettyPrinter(indent=4)

def recursiveCounter(color_dict, bag_color, running_total = 0, multiplier = 1):
    if not color_dict[bag_color]:
        return multiplier
    total = multiplier
    for color in color_dict[bag_color]:
        total += recursiveCounter(color_dict, color, 0, multiplier*color_dict[bag_color][color])
    return total

def b(input):
    color_dict = {}
    for line in input:
        color, contains = parseLine(line)
        if color in color_dict:
            print("COLOR ALREADY DETECTED", color)
            return None
        color_dict[color] = contains
    return recursiveCounter(color_dict, 'shiny gold') - 1
