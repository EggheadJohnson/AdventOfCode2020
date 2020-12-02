import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

total = 0

for line in inpt:
    r, c, pw = line.split(' ')
    r = list(map(int, r.split('-')))
    c = c[:-1]
    pw = pw.strip()
    # print(r, c, pw)

    spot_one = False
    spot_two = False

    if len(pw) >= r[0] and pw[r[0]-1] == c:
        spot_one = True

    if len(pw) >= r[1] and pw[r[1]-1] == c:
        spot_two = True

    if spot_one ^ spot_two:
        total += 1

print(total)
