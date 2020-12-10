import pprint
pp = pprint.PrettyPrinter(indent=4)

def b(input):
    input = [ int(i) for i in input ]
    input.append(0)
    input = sorted(input)
    input.append(input[-1] + 3)
    # pp.pprint(input)
    current_streak = 0
    streak_ctrs = {}
    for i, c in enumerate(input[:-1]):
        diff = input[i+1] - input[i]
        if diff == 1:
            current_streak += 1
        elif diff == 3:
            streak_ctrs[current_streak] = streak_ctrs.get(current_streak, 0) + 1
            current_streak = 0
    pp.pprint(streak_ctrs)
    return 2**streak_ctrs[2] * 4**streak_ctrs[3] * 7**streak_ctrs[4]
