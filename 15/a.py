
def a(input):
    dct = {}
    for i, n in enumerate(input):
        dct[n] = i
        # print(i, n)
    prev = input[-1]
    curr = 0
    for i in range(len(input), 30000000):
        if i%300000 == 0:
            print(i)
        prev = curr
        if prev in dct:
            curr = i - dct[prev]
        else:
            curr = 0
        dct[prev] = i
        # print(i, prev, curr)
    return prev
