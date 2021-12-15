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

def makeMove(move, pos):
    moveDict = {
        'e': (1, 0),
        'w': (-1, 0),
        'nw': (-0.5, 1),
        'sw': (-0.5, -1),
        'ne': (0.5, 1),
        'se': (0.5, -1)
    }
    return (pos[0] + moveDict[move][0], pos[1] + moveDict[move][1])

def runLine(line):
    pos = (0, 0)
    for move in parseLine(line):
        pos = makeMove(move, pos)
    return pos

def findNeighborValues(tile):
    return [
        (tile[0] + 1, tile[1]),
        (tile[0] - 1, tile[1]),
        (tile[0] + 0.5, tile[1] + 1),
        (tile[0] - 0.5, tile[1] + 1),
        (tile[0] + 0.5, tile[1] - 1),
        (tile[0] - 0.5, tile[1] - 1),
    ]

def loadTiles(input):
    tileDict = {}
    tileColorFlipper = {
        'black': 'white',
        'white': 'black'
    }
    for line in input:
        tilePos = runLine(line)
        if tilePos not in tileDict:
            tileDict[tilePos] = 'black'
        else:
            tileDict[tilePos] = tileColorFlipper[tileDict[tilePos]]
    return tileDict

def addAdjacentTilesToDict(tileDict):
    tilesToAdd = set()
    for tile in tileDict:
        neighbors = findNeighborValues(tile)
        tilesToAdd = tilesToAdd | set(neighbors)
    for tile in tilesToAdd:
        if tile not in tileDict:
            tileDict[tile] = 'white'
    return tileDict

def takeSingleStep(tileDict):
    tileColorFlipper = {
        'black': 'white',
        'white': 'black'
    }
    tilesToFlip = set()
    tileDict = addAdjacentTilesToDict(tileDict)
    for tile in tileDict:
        neighbors = findNeighborValues(tile)
        neighborTileColors = [ tileDict[tile] if tile in tileDict else '' for tile in neighbors ]
        tileColor = tileDict[tile]
        if tileColor == 'black' and (neighborTileColors.count('black') == 0 or neighborTileColors.count('black') > 2):
            tilesToFlip.add(tile)
        elif tileColor == 'white' and neighborTileColors.count('black') == 2:
            tilesToFlip.add(tile)
    for tile in tilesToFlip:
        tileDict[tile] = tileColorFlipper[tileDict[tile]]
    return tileDict

def part1(input):
    tileDict = loadTiles(input)
    return list(tileDict.values()).count('black')

def part2(input):
    tileDict = loadTiles(input)
    prevCount = 0
    for i in range(100):
        ct = list(tileDict.values()).count('black')
        print(i, ct, ct-prevCount)
        prevCount = ct
        tileDict = takeSingleStep(tileDict)
    print(list(tileDict.values()).count('black'))
    return None
