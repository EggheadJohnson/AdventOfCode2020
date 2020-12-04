
def a(input):
    rows = []
    pos = (0, 0)
    mov = (1, 3)
    tree_ctr = 0
    for line in input:
        rows.append(line.strip())
    while pos[0] < len(rows):
        if rows[pos[0]][pos[1]] == '#':
            tree_ctr += 1
        pos = (pos[0] + mov[0], (pos[1] + mov[1]) % len(rows[0]))
    return tree_ctr
