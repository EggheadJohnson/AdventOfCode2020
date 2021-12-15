import pprint

pp = pprint.PrettyPrinter(indent=4)

def countTiles(input):
    return len([line for line in input if 'Tile' in line])

def getTileSize(input):
    return

def getTiles(input):
    tiles = {}
    currTile = []
    for line in input:

        if 'Tile' in line:
            key = line[5:-1]
        elif len(line) == 0:
            tiles[key] = currTile
            currTile = []
        else:
            currTile.append(line)
    if len(currTile) > 0:
        tiles[key] = currTile
    return tiles

def flipTile(tile):
    tile.reverse()
    return tile

def encodeTile(tile):
    sides = []
    totals = [0, 0]
    top = list(map(lambda x: 1 if x == '#' else 0, tile[0]))
    for i in range(len(top)):
        totals[0] += top[i] * 2**i
        totals[1] += top[i] * 2**(len(top) - 1 - i)
    sides.extend(totals)
    totals = [0, 0]
    bot = list(map(lambda x: 1 if x == '#' else 0, tile[len(tile) - 1]))
    for i in range(len(bot)):
        totals[0] += bot[i] * 2**i
        totals[1] += bot[i] * 2**(len(bot) - 1 - i)
    sides.extend(totals)
    totals = [0, 0]
    left = list(map(lambda x: 1 if x == '#' else 0, [ row[0] for row in tile ]))
    for i in range(len(left)):
        totals[0] += left[i] * 2**i
        totals[1] += left[i] * 2**(len(left) - 1 - i)
    sides.extend(totals)
    totals = [0, 0]
    right = list(map(lambda x: 1 if x == '#' else 0, [ row[len(row) - 1] for row in tile ]))
    for i in range(len(left)):
        totals[0] += right[i] * 2**i
        totals[1] += right[i] * 2**(len(right) - 1 - i)
    sides.extend(totals)
    totals = [0, 0]
    return sides

def getEncodedTilesWithCount(tiles):
    encodedWithCount = {}
    for tile in tiles:
        encodedWithCount[tile] = {
            'encoding': set(encodeTile(tiles[tile])), # verified that no tile has two identical sides so set is fine
            'count': 0
        }
    return encodedWithCount

def getCountForTile(tileID, encodedTiles):
    targetTile = encodedTiles[tileID]
    total = 0
    for otherTile in [ tile for tile in encodedTiles.keys() if tile != tileID ]:
        total += len(targetTile['encoding'] & encodedTiles[otherTile]['encoding'])
    return total//2

def part1(input):
    print(countTiles(input))
    tiles = getTiles(input)
    sampleTile = list(tiles.values())[0]
    encodedTilesWithCount = getEncodedTilesWithCount(tiles)

    for tile in encodedTilesWithCount:
        encodedTilesWithCount[tile]['count'] = getCountForTile(tile, encodedTilesWithCount)

    # print('count:', getCountForTile('1427', encodedTilesWithCount))
    # pp.pprint(encodedTilesWithCount)
    product = 1
    for tile in encodedTilesWithCount:
        if encodedTilesWithCount[tile]['count'] == 2:
            product *= int(tile)
    # print('Tile size: {} tall by {} wide'.format(len(sampleTile), len(sampleTile[0])))
    # pp.pprint(sampleTile)
    # print(encodeTile(sampleTile))
    return product

def part2(input):
    return None
