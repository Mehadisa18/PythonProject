# For comments in python use #
# import sys is used to import library of system functions

# Displaying maximum int in python2
#import sys
#print(sys.maxint)
# This doesnt work in python3

a = 123394954909685650579467974068098547607909670979795724675378399999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print(a)
print(type(a)) # type() is used to find out the type of any value

a="message"
print(type(a))

# In python3 we have int, float and complex numbers.
# here for complex numbers we use j instead of i 
# say c = 2 + 3j
# lets create some numbers.

b = 23.78 # float
c= 23 + 3j # complex number

print(type(b))
print(type(c))
print (c.real)
print(c.imag)
print("complex numbers"+str(c)) # for concatenation the values of different datatypes have to be converted into
                                # strings before printing. use str() function for that.