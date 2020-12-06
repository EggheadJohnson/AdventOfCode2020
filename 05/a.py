def fromBinary(str, one, zero):
    #  0  1  0  1  1  0  0
    #  64 32 16 8  4  2  1
    p = len(str) - 1
    base_ten = 0
    power_dict = { one: 1, zero: 0 }
    for c in str:
        base_ten += 2**p * power_dict[c]
        p -= 1
    return base_ten

def a(input):
    m = -1
    for line in input:
        row = fromBinary(line[:7], 'B', 'F')
        col = fromBinary(line[7:], 'R', 'L')
        if row * 8 + col > m:
            m = row * 8 + col
    return m
