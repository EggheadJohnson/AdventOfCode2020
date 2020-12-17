def buildBlankThreeSpace(x, y, buffer_size = 20):
    hypercube = []
    for wi in range(1 + buffer_size):
        cube = []
        for zi in range(1 + buffer_size):
            level = []
            for xi in range(x+buffer_size):
                row = []
                for yi in range(y+buffer_size):
                    row.append('.')
                level.append(row)
            cube.append(level)
        hypercube.append(cube)
    return hypercube

def printThreeSpace(four_space):
    for level in four_space:
        for row in level:
            print(row)
        print()

def placeStartInMiddle(starts, four_space):
    w = len(four_space) // 2
    z = len(four_space) // 2
    x = len(four_space[0]) // 2 - len(starts) // 2
    y = len(four_space[0][0]) // 2 - len(starts) // 2

    for i, row in enumerate(starts):
        for j, spot in enumerate(row):
            # print(i, j, x, y, z, spot)
            four_space[w][z][x+i][y+j] = spot
    return four_space

def buildCombinations():
    combos = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i != 0 or j != 0 or k != 0 or l != 0:
                        combos.append( (i, j, k, l) )
    return combos

def determineIfShouldFlip(spot, four_space):
    # print(spot, four_space)
    spot_status = four_space[spot[0]][spot[1]][spot[2]][spot[3]]
    combos = buildCombinations()
    total_on = 0
    # print(combos)
    for combo in combos:
        # print(spot[0] + combo[0], spot[1] + combo[1], spot[2] + combo[2])
        if spot[0] + combo[0] >= 0 and spot[0] + combo[0] < len(four_space) and spot[1] + combo[1] >= 0 and spot[1] + combo[1] < len(four_space[0]) and spot[2] + combo[2] >= 0 and spot[2] + combo[2] < len(four_space[0][0])  and spot[3] + combo[3] >= 0 and spot[3] + combo[3] < len(four_space[0][0][0]) and four_space[spot[0] + combo[0]][spot[1] + combo[1]][spot[2] + combo[2]][spot[3] + combo[3]] == '#':
            total_on += 1
    # print(spot, spot_status, total_on)
    if spot_status == '#':
        # print(total_on != 2, total_on != 3, total_on != 2 and total_on != 3)
        return total_on != 2 and total_on != 3
    return total_on == 3

def takeSingleStep(four_space):
    flippable = set()
    for w, cube in enumerate(four_space):
        for z, level in enumerate(cube):
            for x, row in enumerate(level):
                for y, c in enumerate(row):
                    # if (z, x, y) == (1, 3, 1):
                        # print('hello')
                        # print(determineIfShouldFlip((z, x, y), four_space))
                    if determineIfShouldFlip((w, z, x, y), four_space):
                        # print('adding', (z, x, y))
                        flippable.add((w, z, x, y))
    flipper = {
        '.': '#',
        '#': '.'
    }
    # print(flippable)
    for f in flippable:
        # print(f, four_space[f[0]][f[1]][f[2]], flipper[four_space[f[0]][f[1]][f[2]]])
        four_space[f[0]][f[1]][f[2]][f[3]] = flipper[four_space[f[0]][f[1]][f[2]][f[3]]]
    return four_space

def totalActive(four_space):
    total = 0
    for w in four_space:
        for z in w:
            for x in z:
                for y in x:
                    if y == '#':
                        total += 1
    return total


def b(input):
    # printThreeSpace(placeStartInMiddle(input, buildBlankThreeSpace(3, 3)))
    four_space = placeStartInMiddle(input, buildBlankThreeSpace(len(input), len(input[0])))
    # determineIfShouldFlip((1, 3, 1), four_space)
    # printThreeSpace(four_space)
    for i in range(6):
        takeSingleStep(four_space)
    # printThreeSpace(four_space)
    return totalActive(four_space)
