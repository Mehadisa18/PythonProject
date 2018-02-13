# functions

"""THIS IS A DOC STRING... MAINLY USED FOR DOCUMENTATION"""
def Area():
    print("area")

Area()

# Can have aruguments and return types

import math

def volume(r):
    return (4/3 * math.pi* pow(r,3))

print(volume(3))

# we can have any number of arguments. While calling we must
# make sure that we pass all the required parameters

#volume() # gives error

# keyword arguments are default arguments 

def height_to_cm(feet=0, inches=0):
    in_to_cm = inches*2.54
    feet_to_cm = feet*12*2.54
    return in_to_cm+feet_to_cm

height_to_cm() # here nothing is displayed as we are not printing it
print(height_to_cm()) # returns 0 as no values are passed
print(height_to_cm(3,3))# considers position and takes the arguments
print(height_to_cm(inches=0,feet=3)) # takes the arguments as per the names

# while defining functions with both required arguments and default arguments,
# the default arguments must be defined at the end

# two arguments must not be of same name
def ex_func( r,h=0,p=0):
    return "hello"