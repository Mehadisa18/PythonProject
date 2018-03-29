# Arithmetic operations follow simple rules of casting
# For Version 2
# similar to c, while performing arithmetic operations, the values are casted to wider types.
# The hierarchy goes as follows from narrower to wider types:
# int ---> Long ---> float ---> complex
# Always remember reverse is never possible. i.e a wider data type value cannot be converted into narrower type value 


a = 23
b = 2.3
a1= 1
b1=10
c= 2+3j
d1=a1/b1
print(d1)
d = 2.0/20
print(d) # here even though a is int, it is converted into float before the arithmetic operation is performed.


# In version 2, like all programming languages, the division of two whole numbers in python returns the quotient
# However, this is not the case with python 3.
# In python 3 when two whole numbers are divided the result is a float even when the remainder of the division is 0
e = 23/5
print(e) 

f= 25/5
f1=5.5/25
f2=5.0/50
print (f)
print(f1)
print(f2)

#----------------------------------------------------------------------
print("Doubt -------------------------------------")
#why is it 0.09999 in one case and 0.1 in another.
t=2.3/23
m=2.5/25
print(t)
print(m)
print("-----------------------------------------------")
#------------------------------------------------------------------------

#In order to obtain the final remainder we use % operator
g = 25%5
print(g)

# In order obtain the quotient we use // operator
# This is also called as floor division
h= 23 // 5
print (h)

#lets see how complex number division occurs

i = 23+3j
r = 23
print(i.real) # Here we can see that even though we give whole numbers, python stores the real and imaginary parts of
              # complex numbers as floats

print(i/r)

# lets do complex by complex
n = 22+2j
print(i/n)
# conjugate technique




# division by 0 

#f = 67/0  ### This gives fatal error [divide by 0 error]
#print(f)
