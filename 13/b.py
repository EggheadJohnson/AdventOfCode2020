from math import sqrt

def primeFactors(n):
    i = 2
    factors = {}
    while i <= sqrt(n):
        if n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n = n // i
            i = 2
        else:
            i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def minMul(numbers):
    factors = {}
    for n in numbers:
        pf = primeFactors(n)
        for k in pf:
            if k not in factors:
                factors[k] = pf[k]
            elif pf[k] > factors[k]:
                factors[k] = pf[k]
    total = 1
    for k in factors:
        total *= k**factors[k]
    return factors, total

# print(minMul((2, 3, 4)))
# print(minMul((3, 5, 7)))

def allHappy(l, i):
    for j, n in enumerate(l):
        if n != 'x':
            if (i * l[0] + j) % l[j] != 0:
                return False
    return True

def dumbListToAnswer(l, vals = range(10000)):
    for i in vals:
        if allHappy(l, i):
            return i*l[0]

def findNext(start, step, offset, divisor):
    curr = start
    while (curr + offset) % divisor != 0:
        curr += step
    return curr

def b(input):

    # buses = [ int(bus) for bus in input[1].split(',') if bus != 'x' ]
    # mm = minMul(buses)
    # print(mm)
    intput = []
    for i in input[1].split(','):
        if i != 'x':
            intput.append(int(i))
        else:
            intput.append('x')
    start = None
    step = None
    seen_nums = []
    for i, c in enumerate(intput):
        if c != 'x':
            seen_nums.append(c)
            if start == None:
                start = c
                step = c
            start = findNext(start, step, i, c)
            step = minMul(seen_nums)[1]
    return start
    # answer = dumbListToAnswer(intput, range(1000000))
    # return answer, mm[1] - answer
