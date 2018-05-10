"""
unit test case file is written seperately.

This file contains actual code that needs to be tested 

lets write a simple circle area function
"""
from math import pi

def circle_area(r):
    if(type(r) not in [float,int]):
        raise TypeError("The type of radius not allowed")
    if(r<0):
        raise ValueError("radius cannot be negative")
    return pi*r*r

input_list = [2,0.0,-2,3+4j,True,"radius"]

for i in input_list:
    print("radius: ",i," area: ",circle_area(i)) # error for last value

"""
output
radius:  2  area:  12.566370614359172
radius:  0.0  area:  0.0
radius:  -2  area:  12.566370614359172
radius:  (3+4j)  area:  (-21.991148575128552+75.39822368615503j)
radius:  True  area:  3.141592653589793
Traceback (most recent call last):
File "27_Unit_tests.py", line 16, in <module>
print("radius: ",i," area: ",circle_area(i))
File "27_Unit_tests.py", line 11, in circle_area
return pi*r*r
TypeError: can't multiply sequence by non-int of type 'float'
lets write test cases for testing this function

"""