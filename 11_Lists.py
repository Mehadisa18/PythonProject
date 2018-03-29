# Lists follow order but duplicates are allowed
a = list(['a',1,2,3,3+5j])
print(a)
b= [1,2,3,'e','t','7']
print(b)
b.append('o')
print(b)

# List can be defined using list keyword or by simply using square braces



print(b[0])

# A list can be wrapped once
# list[-1] gives the last element 

print(b[-1])
print(b[-2])

# REMEMBER : A LIST CAN BE WRAPPED ONLY ONCE

# Slicing the lists

# slicing lists : first param --> starting of the list to be sliced
                  # second param ---> ending of list + 1

print(b[0:3]) # the element at index 3 is excluded [e will be excluded]

# concatenating the list

print(a+b) # order matters

# repetetion is also allowed

b.append(2)
print(b)

# a list can also be reversed 
print(b.reverse()) # returning None : DOUBT ######
