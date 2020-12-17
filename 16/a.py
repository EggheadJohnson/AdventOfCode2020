
def parseNamedOptions(line):
    name, options = line.split(': ')
    options = options.split(' or ')
    option_set = set()
    for o in options:
        l, h = o.split('-')
        l = int(l)
        h = int(h) + 1
        option_set = option_set.union(set(range(l, h)))
    return name, option_set

def parseTicket(line):
    fields = [ int(n) for n in line.split(',') ]
    return fields

def parseInput(input):
    step = 0
    options = {}
    nearby_tickets = []
    your_ticket = None
    for line in input:
        if len(line) == 0:
            step += 1
        elif step == 0:
            name, option_set = parseNamedOptions(line)
            options[name] = option_set
        elif step == 1:
            if line == 'your ticket:':
                continue
            your_ticket = parseTicket(line)
        elif step == 2:
            if line == 'nearby tickets:':
                continue
            nearby_tickets.append(parseTicket(line))
    options['all_options'] = set()
    for k in options:
        if k != 'all_options':
            options['all_options'] = options['all_options'].union(options[k])
    return options, your_ticket, nearby_tickets

def a(input):
    options, your_ticket, nearby_tickets = parseInput(input)
    # print(options,your_ticket, nearby_tickets)
    total = 0
    for ticket in nearby_tickets:
        for i in ticket:
            if i not in options['all_options']:
                # print(i)
                total += i
    return total
