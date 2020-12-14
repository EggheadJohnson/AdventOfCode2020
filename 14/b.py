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
        if c != '0':
            bin_val = bin_val[:i] + c + bin_val[i+1:]
    return bin_val

def enumerateOptions(bin_val):
    options = []
    ct = bin_val.count('X')
    swappable = ''
    for c in bin_val:
        if c == 'X':
            swappable += '{}'
        else:
            swappable += c
    for i in range(2**ct):
        bin_str = toStringBaseTwo(i, ct)
        options.append(swappable.format(*bin_str))
    return options

def transformVal(n, bitmask):
    n = toStringBaseTwo(n)
    n = applyBitmask(bitmask, n)
    return enumerateOptions(n)

def b(input):
    memory_spots = {}
    for line in input:
        if line[:3] == 'mas':
            bitmask = line.split(' = ')[1]
        elif line[:3] == 'mem':
            mem_loc = int(line.split(' = ')[0][4:-1])
            for option in transformVal(mem_loc, bitmask):
                val = int(line.split(' = ')[1])
                memory_spots[option] = val
    return sum(memory_spots.values())
