import pprint, re

pp = pprint.PrettyPrinter(indent=4)

def buildRulesDict(input):
    rulesDict = {}
    for line in input:
        if ': ' in line:
            ruleNumber, rule = line.split(': ')
            if '"' in rule:
                rule = rule[1]
            rulesDict[ruleNumber] = rule
    return rulesDict

def getTestStrings(input):
    return [ line for line in input if len(line) > 0 and ': ' not in line ]

def buildREForKey(rulesDict, key):
    rule = rulesDict[key].split(' ')
    ruleOut = []
    for k in rule:
        if k in rulesDict:
            if rulesDict[k] in ('a', 'b'):
                ruleOut.append('(' + rulesDict[k] + ')')
            else:
                ruleOut.append(buildREForKey(rulesDict, k))
        elif k == '|':
            ruleOut.append('|')
    return ruleOut

def flattenRE(reArray):
    flattenedREString = '('
    for i in reArray:
        if isinstance(i, list):
            flattenedREString += flattenRE(i)
        else:
            flattenedREString += i
    flattenedREString += ')'

    return flattenedREString

def part1(input):
    rulesDict = buildRulesDict(input)
    testStrings = getTestStrings(input)
    # pp.pprint(rulesDict)
    # pp.pprint(testStrings)
    reToUse = buildREForKey(rulesDict, '0')
    flattenedREToUse = '^' + flattenRE(reToUse) + '$'
    # print(flattenedREToUse)
    matches = list(filter(lambda x: re.search(flattenedREToUse, x), testStrings))
    # print(len(matches), matches)
    return len(matches)

def part2(input):
    return None
