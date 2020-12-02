import os
from a import a
from b import b

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/input.txt"

inpt = open(input_path, 'r')
print(a(inpt))
inpt = open(input_path, 'r')
print(b(inpt))
