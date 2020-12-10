
def a(input):
    input = [ int(i) for i in input ]
    input.append(0)
    input = sorted(input)
    input.append(input[-1] + 3)
    # print(input)
    ones = 0
    twos = 0
    threes = 0
    for i in range(len(input) - 1):
        diff = input[i + 1] - input[i]
        if diff == 1:
            ones += 1
        elif diff == 2:
            twos += 1
        elif diff == 3:
            threes += 1
    return ones, twos, threes, ones * threes
