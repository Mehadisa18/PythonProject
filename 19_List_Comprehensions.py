"""
We use List comprehensions to utilize the functionality of lists in an easier way """

"""

List comprehension = [value for value in some set if <test case >] ----> we can put as many test cases as we want using and operator """

List1 = [ 2,3,4,5,6,7,8,9]

list_comp = [a for a in List1 if a % 2 == 0]
print(list_comp) 

""" here we are printing all the even numbers """

List2 = [(1,2),(3,4),(4,2),(9,0),(10,11),(7,2)]

# lets display all the x co-ordinates whose y co-ordinates are 2

list_comp2 = [a for (a,b) in List2 if b==2]
print(list_comp2)

list_comp3 = [x**2 for x in range(1,101) if x % 2 == 0]
print(list_comp3) # this returns squares of all the even numbers from 1 to 100

# cartesian product

A = [2,3,4,5]
B= [6,7,8,9]
cp = [(a,b) for a in A for b in B]
print(cp)

trial = [(a,b,c) for a in A for b in B for c in A]
print (len(trial))
print(trial)
