import sys
import random

file_name = sys.argv[1]

file = open(file_name,"wb")

# Write random lines of random numbers

for line in range(random.randint(0,100)):
    file.write("%s\n" % random.random())

file.close()
