from a import parseLine
from b import recursiveCounter
import pprint
pp = pprint.PrettyPrinter(indent=4)

def c(input):
    color_dict = {}
    for line in input:
        color, contains = parseLine(line)
        if color in color_dict:
            print("COLOR ALREADY DETECTED", color)
            return None
        color_dict[color] = contains
    max_color = None
    min_color = None
    color_ctr = {}
    for color in color_dict:
        color_ctr[color] = recursiveCounter(color_dict, color) - 1
        if not max_color or color_ctr[color] > color_ctr[max_color]:
            max_color = color
        if not min_color or color_ctr[color] < color_ctr[min_color]:
            min_color = color
    pp.pprint(color_ctr)
    return max_color, color_ctr[max_color], min_color, color_ctr[min_color]
