import pprint

pp = pprint.PrettyPrinter(indent=4)

def findLoopSize(target, multiplier=7, modulizer=20201227):
    c = 0
    i = 1
    while i != target:
        i *= multiplier
        i %= modulizer
        c += 1
        # print(c, i)
    return c

def performLoop(subjectNumber, loopsize, modulizer=20201227):
    print(subjectNumber, loopsize)
    i = 1
    for j in range(loopsize):
        i *= subjectNumber
        i %= modulizer
        # print(j, i)
    return i

def part1(input):
    cardPK = int(input[0])
    doorPK = int(input[1])
    cardLoopSize = findLoopSize(cardPK)
    doorLoopSize = findLoopSize(doorPK)
    return performLoop(doorPK, cardLoopSize)

def part2(input):
    return None
