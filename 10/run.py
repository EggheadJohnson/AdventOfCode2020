import os
from a import a
from b import b

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/input.txt"

inpt = [ line.strip() for line in open(input_path, 'r')]

print("result A:", a(inpt))
print("result B:", b(inpt))
