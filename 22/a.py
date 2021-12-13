import pprint
pp = pprint.PrettyPrinter(indent=4)

def buildPlayerDecks(input):
    player1 = input[1:input.index('')]
    player2 = input[input.index('')+2:]


    player1 = list(map(int, player1))
    player2 = list(map(int, player2))

    return player1, player2

def takeOneStep(player1, player2):
    player1_card = player1.pop(0)
    player2_card = player2.pop(0)

    if player1_card > player2_card:
        player1.extend([player1_card, player2_card])
    if player2_card > player1_card:
        player2.extend([player2_card, player1_card])

def playFullGame(player1, player2):
    while player1 and player2:
        takeOneStep(player1, player2)

def calculatePlayerScore(player):
    total = 0
    for i in range(len(player), 0, -1):
        total += i * player[len(player) - i]
    return total

def a(input):
    # pp.pprint(input)
    player1, player2 = buildPlayerDecks(input)
    # pp.pprint(player1)
    # pp.pprint(player2)
    playFullGame(player1, player2)
    # pp.pprint(player1)
    # pp.pprint(player2)
    if player1:
        return calculatePlayerScore(player1)
    return calculatePlayerScore(player2)
