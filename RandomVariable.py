#!/usr/bin/python3

import random

a = [1, 2, 3, 4, 5, 6]

print ("#################################################\n")

print (random.choice(a))
print (random.randrange(0, 100, 4))
print (random.random())
print (random.seed(3.141592657))
random.shuffle(a)
print (a)
print (random.uniform(1, 10))

print ("\n#################################################")