def toStringBaseTwo(n, left_pad = 36):
    output = ''
    while n > 0:
        output = str(n%2) + output
        n //= 2
    while len(output) < left_pad:
        output = '0' + output
    return output

def applyBitmask(bitmask, bin_val):
    for i, c in enumerate(bitmask):
        if c != 'X':
            bin_val = bin_val[:i] + c + bin_val[i+1:]
    return bin_val

def transformVal(n, bitmask):
    bin_val = toStringBaseTwo(n)
    post_bitmask = applyBitmask(bitmask, bin_val)
    return int(post_bitmask, 2)


def a(input):
    memory_spots = {}
    for line in input:
        if line[:3] == 'mas':
            bitmask = line.split(' = ')[1]
        elif line[:3] == 'mem':
            mem_loc = line.split(' = ')[0][4:-1]
            val = int(line.split(' = ')[1])
            val = transformVal(val, bitmask)
            memory_spots[mem_loc] = val

    return sum(memory_spots.values())
