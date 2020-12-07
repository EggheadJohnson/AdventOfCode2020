
def a(input):
    all_sets = []
    group_set = set()
    for line in input:
        if len(line) == 0:
            all_sets.append(group_set)
            group_set = set()
        else:
            for c in line:
                group_set.add(c)
    if len(group_set) != 0:
        all_sets.append(group_set)
    total = 0
    for s in all_sets:
        total += len(s)
    return total
