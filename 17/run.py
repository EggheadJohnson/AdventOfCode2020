import time
import os
from a import a
from b import b

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/input.txt"

inpt = [ line.strip() for line in open(input_path, 'r')]

a_start = time.time()
print("result A:", a(inpt))
a_end = time.time()
print(a_end - a_start)
b_start = time.time()
print("result B:", b(inpt))
b_end = time.time()
print(b_end - b_start)
