"""
The very much awaited lesson is here.

Map - Reduce - Filter

"""

# The map function maps the given function to every element of the list

list1 = [1,2,3,4,5,6,7,8,9,10]

fun1 = lambda x : x+1
# the map function returns the map. In order to get a list we have to use list() again

print(list(map(fun1,list1))) # output : [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# filter function filters out unecessary data
list2 = list1 #here object gets allocated
list2.append("")
list2.append(0)
list2.extend(["",{},[],0.0,0j,0,(),False,None])
print(list2)

print(list(filter(None,list2))) # by using None all the false elements are discarded

# another use of filter
data =[1.1,2,3]
print(list1)
y=5
print(list(filter(lambda x: x>y, data)))


# reduce function

"""
working of a reduce function:
list =[a1, a2, a3,...an]
reduce(f , list)
reduce works as below :
val1 = f(a1,a2)
val2 = f(val1,a3)
val3 = f(val2,a4) and so on and on
"""

# product function
from functools import reduce
list = [1,2,3,4,5]
product = reduce(lambda x,y: x*y, list)
print(product) # 120 
# very clumpsy...used in rare cases



