# python has this amazing interactive feature
dir() # displays all the available modules which contain
      # objects which can be used while coding

#dir("module name") # This gives out the objects and functions in the 
                   # builtins module which can be used 
# help (Object/fun name") : explains the Object

help(pow)

# lets use pow function

print(pow(2,4)) # 2 to the power of 4

# lets use three numbers

print(pow(2,4, 8))

# when three numbers are given the result will always be x**y % z

# we have external modules as well

help('modules')

import math

dir(math)
print(math.radians(180))

# always remember we use dir for finding out all the functions that a module has
# we use help to know how a function works
# never use quotes within dir
# In help() we can use anything

