import os
from a import a
from b import b

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/input.txt"

inpt = [ line.strip() for line in open(input_path, 'r')]
inpt = [ int(i) for i in inpt[0].split(',') ]

print("result A:", a(inpt))
print("result B:", b(inpt))
