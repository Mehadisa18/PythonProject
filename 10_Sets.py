# set : a group of elements where order doesnt matter
# No repetitions in a set

A= set()

A.add(1)
A.add(3)

print(A)

B= set([123,"huma","sajan",True]) # No data type restriction
print(B)

print(123 in B)
print("345" not in B)
print(B)

# Unions and intersections

C =set([1,2,3,4])
D= set([4,5,6,7])
print(C.union(D))
print(D.intersection(C))

# PYTHON SYNTAX IS CASE sensitive :P

# removing from sets
# if element is not present then remove function throws error 
# In such a case discard() can be used.

C.remove(1)
print(C)

#C.remove(7) # remove error

C.discard(7)
print(C)
C.discard(1)
print(C)
C.discard(3)
print(C)

