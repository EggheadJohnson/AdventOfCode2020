from a import parseInput

def isTicketValid(ticket, option_set):
    for n in ticket:
        if n not in option_set:
            return False
    return True

def b(input):
    options, your_ticket, nearby_tickets = parseInput(input)
    possibilities = []
    for i in range(len(your_ticket)):
        possibilities.append(set([ o for o in options.keys() if o != 'all_options' ]))
    # print(possibilities)
    for ticket in [*nearby_tickets, your_ticket]:
        if not isTicketValid(ticket, options['all_options']):
            continue
        for i, n in enumerate(ticket):
            removes = set()
            for field in possibilities[i]:
                if n not in options[field]:
                    removes.add(field)
            for r in removes:
                possibilities[i].remove(r)
    removedSomething = True
    while removedSomething:
        removedSomething = False
        singles = set()
        for p in possibilities:
            if len(p) == 1:
                singles.add(list(p)[0])
        for s in singles:
            for p in possibilities:
                if len(p) > 1 and s in p:
                    removedSomething = True
                    p.remove(s)
    print(possibilities)
    total = 1
    for i, name_set in enumerate(possibilities):
        if 'departure' in list(name_set)[0]:
            total *= your_ticket[i]
    return total
