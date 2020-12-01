import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

row_set = set()

for line in inpt:
    line = int(line)
    row_set.add(line)

for i in row_set:
    for j in row_set:
        if i != j and 2020 - i - j in row_set:
            print(i, j, 2020 - i - j, i * j * (2020 - i - j))
