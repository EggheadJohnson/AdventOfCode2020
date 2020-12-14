
def a(input):
    steps = (
        (1, 0), # north
        (0, 1), # east
        (-1, 0), # south
        (0, -1), # west
    )
    step_ctr = 1
    loc = (0, 0)
    for line in input:
        instruction = line[0]
        amount = int(line[1:])
        if instruction == 'F':
            for i in range(amount):
                loc = (loc[0] + steps[step_ctr][0], loc[1] + steps[step_ctr][1])
        if instruction == 'R':
            step_ctr += amount // 90
            step_ctr %= 4
        if instruction == 'L':
            step_ctr -= amount // 90
            step_ctr %= 4
        if instruction == 'N':
            loc = (loc[0] + amount, loc[1])
        if instruction == 'S':
            loc = (loc[0] - amount, loc[1])
        if instruction == 'E':
            loc = (loc[0], loc[1] + amount)
        if instruction == 'W':
            loc = (loc[0], loc[1] - amount)
    return abs(loc[0]) + abs(loc[1])
