import pprint
from collections import deque
from itertools import islice

pp = pprint.PrettyPrinter(indent=4)

def takeSingleStep(cups):
    curr = cups.popleft()

    next3 = []
    for i in range(3):
        next3.append(cups.popleft())
    destination = curr
    while destination not in cups:
        destination -= 1
        if destination < 1:
            destination += 9
    i = cups.index(destination)
    newCups = deque(islice(cups, 0, i+1))
    newCups.extend(next3)
    newCups.extend(islice(cups, i+1, 1000000))
    newCups.append(curr)
    return newCups

def takeSeveralSteps(cups, stepCount=10):
    for i in range(stepCount):
        cups = takeSingleStep(cups)
        # print(cups)
    return cups

def getOrder(cups):
    i = cups.popleft()
    while i != 1:
        cups.append(i)
        i = cups.popleft()
    return ''.join(map(str, cups))

def getNextTwo(cups):
    i = cups.index(1)
    return islice(cups, i+1, i+3)

def part1(input):
    cups = deque(map(int, list(input[0])))
    # cups = [1, 3, 6, 7, 9, 2, 5, 8, 4]
    print(cups)
    cups = takeSeveralSteps(cups, 100)
    # cups = takeSingleStep(cups)
    print(cups)
    return getOrder(cups)

def part2(input):
    cups = deque(map(int, list(input[0])))
    # cups = [1, 3, 6, 7, 9, 2, 5, 8, 4]
    cups.extend(range(10, 1000001))
    print(len(cups))
    # print(cups)
    cups = takeSeveralSteps(cups, 10000000)
    # cups = takeSingleStep(cups)
    # print(cups)
    i, j = getNextTwo(cups)
    print(i, j)
    return i*j
