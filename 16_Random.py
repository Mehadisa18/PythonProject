# We will discuss about random module in python

import random

#print(dir(random)) # here we explore random module directory.

# we can generate pseudo random numbers with in a given range

# iteration to generate 10 random numbers
for i in range(10):
    print(random.random())


print("-"*70)
# how to provide the range here

# to generate numbers in the range of [4,7)
# here 4 included and 7 excluded
# we first multiply the number by 3 i.e 7-4 =3, here we will get numbers in the range of [0,3) 
# now add 4 to all the numbers which will give us the range [4,7) : here we shift the numbers by 4 values

def my_random(r1,r2):
    for i in range(10):
        print(random.random()*(r2-r1) + r1)


my_random(4,7)
print("-"*70)
my_random(5,7)
print("-"*70)
my_random(6,7)

# to display random values from a set of numbers
# here we use random int

for i in range(10):
    print(random.randint(3,7)) # like dice game

# uniformly distributed numbers can also be generated
print("-"*70)
for i in range(10):
    print(random.uniform(3,6))
print("-"*70)
# Normally distributed numbers can be displayed using normalvariate function
for i in range(10):
    print(random.normalvariate(5,2)) # first param is mean and second param is sd

# to choose among a set of outcomes

outcomes = ["jump","sit","sleep"]
for i in range(10):
    print(random.choice(outcomes))


