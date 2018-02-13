# triangles problem
# finding out the type of the traingle

# This int does not convert string to int.
# Only numbers are allowed.
a = int(input("enter the len of first side"))
b = int(input("enter the len of second side"))
c = int(input("enter the len of third side"))

# A block in the code is determined using the inundation of the code
#unlike java, here there are no flower braces to determine the blocks

if a>0 and b>0 and c>0:
 if(a+b>c and b+c>a and c+a>b): 
    if a!=b and b!=c and a!=c:
     print("Scalene triangle") 
    elif a==b and b==c: #short form of else if
     print("equilateral traingle")
    else:
     print("isosceles triangle")
 else:
     print("not a triangle: according to the measurements")
else:
 print("-ve numbers not allowed")

