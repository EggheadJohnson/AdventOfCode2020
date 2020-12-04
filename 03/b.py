
def b(input):
    possible_moves = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]
    trees = []
    rows = []
    for line in input:
        rows.append(line.strip())
    for mov in possible_moves:

        pos = (0, 0)
        tree_ctr = 0
        while pos[0] < len(rows):
            if rows[pos[0]][pos[1]] == '#':
                tree_ctr += 1
            pos = (pos[0] + mov[0], (pos[1] + mov[1]) % len(rows[0]))
        print(mov, tree_ctr)
        trees.append(tree_ctr)
    result = 1
    for t in trees:
        result *= t
    return result    
