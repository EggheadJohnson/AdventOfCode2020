import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

row_set = set()

for line in inpt:
    line = int(line)
    if 2020 - line in row_set:
        print(line, 2020 - line, line * (2020 - line))
    row_set.add(line)
