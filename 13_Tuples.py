# Tuples are similar to Lists. They maintain order. However Tuples have less
# methods when compared to Lists. hence they occupy less space
# A Tuple object definitely occupies less space when compared to Lists

List1 = [1,'b','c','d','e']
Tuple1=(1,'b','c','d','e')
print(List1)
print(Tuple1)

import sys

#print(dir(sys))

print(dir(List1))
print(80*"_")
print(dir(Tuple1))

# A tuple is immutable. Just like a string in java

# The time taken to create a million tuples is considerably less than the time
# taken to create a million elements of the list.
# This will make a lot of difference while processing billions of records
print(80*"_")
import sys
print("list size : ",sys.getsizeof(List1))
print("tuple size : ",sys.getsizeof(Tuple1))

# WE CAN SEE THAT LIST OCCUPIES MORE SPACE THAN TUPLE
print(80*"*")
import timeit
#help(timeit)
time_list = timeit.timeit(stmt="[1,2,3,4]",number=1000000)
#help(timeit)
time_tuple = timeit.timeit(stmt="(1,2,3,4)",number=1000000)

print("timelist: ",time_list)
print("time tuple : ",time_tuple)
# We can see that tuple takes less time to get executed

emptytuple = ()
singletuple =('a')
twotuples =('b','c')
print(emptytuple)
print(singletuple) # here a is not considered as tuple. It is considered as a string
print(twotuples)

print(type(singletuple)) 
singletuple1=('a',)
print(singletuple1) # Now it will be considered as tuple
print(type(singletuple1))

# reason for eccentricity

t=(1,2,3,4)
print(t[0])
print(t[1])
a,b,c,d = t
print(a) # even this works where we can get each value in single line
         # if comma is used, then it will help for seperation
# a,b,c = t # value error. values wont match

