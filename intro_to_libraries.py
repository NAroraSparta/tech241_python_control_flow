# Libraries

#Libraries are collections of functions (pre-built code) that do a job for you.
# We can import these libraries to make our own code easier to understand, be less complex and faster to write.

#######  Method 1 to import any library #################
# import random as rand
# print(rand.randint(1, 100))

#######  Method 2 to import any library #################
# from random import randint
# print(randint(1, 100))
#
# ####### Method 3 to import multiple libraries #################
from random import randint, random, randrange
import math

print(random())

num_float = 23.22
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)


