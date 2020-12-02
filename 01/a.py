
def a(input):
    row_set = set()

    for line in input:
        line = int(line)
        if 2020 - line in row_set:
            return line, 2020 - line, line * (2020 - line)
        row_set.add(line)
