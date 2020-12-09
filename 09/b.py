from a import a

def b(input):
    target = a(input, 25)
    input = [ int(i) for i in input ]
    l = 2
    print(target)
    while True:
        print(l)
        for i in range(len(input) - (l - 1)):
            if sum(input[i:i+l]) == target:
                smallest = min(input[i:i+l])
                largest = max(input[i:i+l])
                return smallest, largest, smallest+largest
        l += 1
