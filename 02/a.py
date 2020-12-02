import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

total = 0

for line in inpt:
    r, c, pw = line.split(' ')
    r = list(map(int, r.split('-')))
    c = c[:-1]

    # print(r, c, pw)

    if pw.count(c) >= r[0] and pw.count(c) <= r[1]:
        total += 1

print(total)
