def buildBlankThreeSpace(x, y, buffer_size = 14):
    cube = []
    for zi in range(1 + buffer_size):
        level = []
        for xi in range(x+buffer_size):
            row = []
            for yi in range(y+buffer_size):
                row.append('.')
            level.append(row)
        cube.append(level)
    return cube

def printThreeSpace(three_space):
    for level in three_space:
        for row in level:
            print(row)
        print()

def placeStartInMiddle(starts, three_space):
    z = len(three_space) // 2
    x = len(three_space[0]) // 2 - len(starts) // 2
    y = len(three_space[0][0]) // 2 - len(starts) // 2

    for i, row in enumerate(starts):
        for j, spot in enumerate(row):
            # print(i, j, x, y, z, spot)
            three_space[z][x+i][y+j] = spot
    return three_space

def buildCombinations():
    combos = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i != 0 or j != 0 or k != 0:
                    combos.append( (i, j, k) )
    return combos

def determineIfShouldFlip(spot, three_space):
    # print(spot, three_space)
    spot_status = three_space[spot[0]][spot[1]][spot[2]]
    combos = buildCombinations()
    total_on = 0
    # print(combos)
    for combo in combos:
        # print(spot[0] + combo[0], spot[1] + combo[1], spot[2] + combo[2])
        if spot[0] + combo[0] >= 0 and spot[0] + combo[0] < len(three_space) and spot[1] + combo[1] >= 0 and spot[1] + combo[1] < len(three_space[0]) and spot[2] + combo[2] >= 0 and spot[2] + combo[2] < len(three_space[0][0]) and three_space[spot[0] + combo[0]][spot[1] + combo[1]][spot[2] + combo[2]] == '#':
            total_on += 1
    # print(spot, spot_status, total_on)
    if spot_status == '#':
        # print(total_on != 2, total_on != 3, total_on != 2 and total_on != 3)
        return total_on != 2 and total_on != 3
    return total_on == 3

def takeSingleStep(three_space):
    flippable = set()
    for z, level in enumerate(three_space):
        for x, row in enumerate(level):
            for y, c in enumerate(row):
                # if (z, x, y) == (1, 3, 1):
                    # print('hello')
                    # print(determineIfShouldFlip((z, x, y), three_space))
                if determineIfShouldFlip((z, x, y), three_space):
                    # print('adding', (z, x, y))
                    flippable.add((z, x, y))
    flipper = {
        '.': '#',
        '#': '.'
    }
    # print(flippable)
    for f in flippable:
        # print(f, three_space[f[0]][f[1]][f[2]], flipper[three_space[f[0]][f[1]][f[2]]])
        three_space[f[0]][f[1]][f[2]] = flipper[three_space[f[0]][f[1]][f[2]]]
    return three_space

def totalActive(three_space):
    total = 0
    for z in three_space:
        for x in z:
            for y in x:
                if y == '#':
                    total += 1
    return total


def a(input):
    # printThreeSpace(placeStartInMiddle(input, buildBlankThreeSpace(3, 3)))
    three_space = placeStartInMiddle(input, buildBlankThreeSpace(len(input), len(input[0])))
    # determineIfShouldFlip((1, 3, 1), three_space)
    # printThreeSpace(three_space)
    for i in range(6):
        takeSingleStep(three_space)
    # printThreeSpace(three_space)
    return totalActive(three_space)
