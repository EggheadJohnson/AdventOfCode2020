from a import fromBinary
def b(input):
    all_seats = []
    for line in input:
        row = fromBinary(line[:7], 'B', 'F')
        col = fromBinary(line[7:], 'R', 'L')
        all_seats.append(row * 8 + col)
    all_seats = sorted(all_seats)
    for i in range(len(all_seats) - 1):
        if all_seats[i] + 1 != all_seats[i + 1]:
            return all_seats[i] + 1
