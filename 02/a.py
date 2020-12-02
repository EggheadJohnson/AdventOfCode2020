
def a(input):
    total = 0

    for line in input:
        r, c, pw = line.split(' ')
        r = list(map(int, r.split('-')))
        c = c[:-1]

        if pw.count(c) >= r[0] and pw.count(c) <= r[1]:
            total += 1

    return total
