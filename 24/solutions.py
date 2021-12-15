import pprint

pp = pprint.PrettyPrinter(indent=4)

def parseLine(line):
    i = 0
    output = []
    while i < len(line):
        if line[i] in ('n', 's'):
            output.append(line[i:i+2])
            i += 1
        else:
            output.append(line[i])
        i += 1
    return output

def part1(input):
    print(parseLine(input[0]))
    return None

def part2(input):
    return None
