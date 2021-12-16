import pprint
pp = pprint.PrettyPrinter(indent=4)

def flatten(line, reducer):
    if '(' not in line:
        return reducer(line)
    while '(' in line:
        start = None
        subLine = ''
        end = None
        parenCtr = 0
        for i in range(len(line)):
            if line[i] == ')':
                parenCtr -= 1
                if parenCtr == 0:
                    end = i
                    line = line[:start] + str(flatten(subLine.strip(), reducer)) + line[end+1:]
                    break
            if start is not None and end is None:
                subLine += line[i]
            if line[i] == '(':
                parenCtr += 1
                if start is None:
                    start = i

    return reducer(line)

def inOrderReducer(line):
    line = line.split(' ')
    total = int(line[0])
    i = 1
    while i < len(line):
        if line[i] == '+':
            total += int(line[i+1])
            i += 1
        elif line[i] == '*':
            total *= int(line[i+1])
            i += 1
        else:
            print("I was not expecting this. {}".format(line[i]))
        i += 1
    return total

def plusFirstReducer(line):
    line = line.split(' ')
    while '+' in line:
        i = line.index('+')
        tempLine = line[:i-1]
        tempLine.append(str(int(line[i-1]) + int(line[i+1])))
        tempLine.extend(line[i+2:])
        line = tempLine
    return inOrderReducer(' '.join(line))

def part1(input):
    return sum([flatten(line, inOrderReducer) for line in input])

def part2(input):
    return sum([flatten(line, plusFirstReducer) for line in input])
