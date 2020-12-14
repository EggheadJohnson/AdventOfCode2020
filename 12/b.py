# 10561 is too low
def b(input):
    ship = (0, 0)
    waypt = (1, 10)
    for line in input:
        instruction = line[0]
        amount = int(line[1:])
        if instruction == 'F':
            for i in range(amount):
                ship = (ship[0] + waypt[0], ship[1] + waypt[1])
        if instruction == 'R':
            for i in range(amount // 90):
                waypt = (-1 * waypt[1], waypt[0])
        if instruction == 'L':
            for i in range(amount // 90):
                waypt = (waypt[1], -1 * waypt[0])
        if instruction == 'N':
            for i in range(amount):
                waypt = (waypt[0] + 1, waypt[1])
        if instruction == 'S':
            for i in range(amount):
                waypt = (waypt[0] - 1, waypt[1])
        if instruction == 'E':
            for i in range(amount):
                waypt = (waypt[0], waypt[1] + 1)
        if instruction == 'W':
            for i in range(amount):
                waypt = (waypt[0], waypt[1] - 1)
        # print(ship, waypt)
    return abs(ship[0]) + abs(ship[1])
