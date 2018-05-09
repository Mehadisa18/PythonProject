"""
Now we will learn how to use lambda expressions in python

"""

"""
Lambda functions are the anonymous functions which just do the work but
 wont have a name """

 # named lambda functions

g = lambda k: k+2

print(g(2)) # 2+2 = 4 

"""
lambda functions cannot be used for multiple lines of code

"""

# anonymous lambda functions

names = ["huma m l", "sajan chand palagiri","nouheera kalluri","nyamathulla lepakshi"]

print(names.sort(key= lambda name: name.split(" ")[-1].lower()))

print(names)

#to create functions
def quadfunc(a,b,c):
    return lambda x: a*x*x + b*x+c

print(quadfunc(2,3,4)(1))
f= quadfunc(1,1,1)
print(f(1))


