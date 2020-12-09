def isValid(window, target):
    for w in window:
        if target - w != w and target - w in window:
            return target - w
def a(input, size = 25):
    input = [ int(i) for i in input ]
    window = set(input[:size])
    c = size
    for i in range(c, len(input)):
        if not isValid(window, input[c]):
            return input[c]
        window.remove(input[c - size])
        window.add(input[c])
        c += 1
    return None
