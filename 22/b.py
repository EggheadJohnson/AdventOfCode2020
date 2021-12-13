import pprint
pp = pprint.PrettyPrinter(indent=4)
seen_set = set()


def buildPlayerDecks(input):
    player1 = input[1:input.index('')]
    player2 = input[input.index('')+2:]


    player1 = list(map(int, player1))
    player2 = list(map(int, player2))

    return player1, player2

def takeOneStep(player1, player2, depth):
    player1_card = player1.pop(0)
    player2_card = player2.pop(0)

    if len(player1) >= player1_card and len(player2) >= player2_card:
        player1_sub = player1[:player1_card]
        player2_sub = player2[:player2_card]
        playRecursiveGame(player1_sub, player2_sub, depth+1)
        if player1_sub:
            player1.extend([player1_card, player2_card])
        if player2_sub:
            player2.extend([player2_card, player1_card])
    else:
        if player1_card > player2_card:
            player1.extend([player1_card, player2_card])
        if player2_card > player1_card:
            player2.extend([player2_card, player1_card])

def calculatePlayerScore(player):
    total = 0
    for i in range(len(player), 0, -1):
        total += i * player[len(player) - i]
    return total

def playRecursiveGame(player1, player2, depth=0):

    while player1 and player2:
        if depth == 0:
            state_tuple = (tuple(player1), tuple(player2))
            # print(state_tuple)
            if state_tuple in seen_set:
                return 'player1_by_loop'
            seen_set.add(state_tuple)
        takeOneStep(player1, player2, depth)
    return None

def b(input):
    player1, player2 = buildPlayerDecks(input)
    result = playRecursiveGame(player1, player2)
    pp.pprint(player1)
    pp.pprint(player2)
    pp.pprint(result)
    if result == 'player1_by_loop' or player1:
        return calculatePlayerScore(player1)
    return calculatePlayerScore(player2)
