
def b(input):

    row_set = set()

    for line in input:
        line = int(line)
        row_set.add(line)

    for i in row_set:
        for j in row_set:
            if i != j and 2020 - i - j in row_set:
                return i, j, 2020 - i - j, i * j * (2020 - i - j)
