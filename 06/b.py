
def parseGroupResult(group_dict, group_ctr):
    group_result = []
    for k in group_dict.keys():
        if group_dict[k] == group_ctr:
            group_result.append(k)
    return group_result

def b(input):
    group_dict = {}
    group_ctr = 0
    all_group_lists = []
    for line in input:
        if len(line) == 0:
            all_group_lists.append(parseGroupResult(group_dict, group_ctr))
            group_dict = {}
            group_ctr = 0
        else:
            for c in line:
                group_dict[c] = group_dict.get(c, 0) + 1
            group_ctr += 1
    if len(group_dict.keys()) != 0:
        all_group_lists.append(parseGroupResult(group_dict, group_ctr))
    total = 0
    for g in all_group_lists:
        total += len(g)
    return total
