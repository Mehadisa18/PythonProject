# Here we will learn about two functions
"""
sort() and sorted() 

sort() : changes the existing list
         cannot be used on a tuple as tuple is immutable

sorted(): creates a new list out of a tuple or a list or a string
what ever may be the input, the output is list """

list1 = ["orange","apple","berry","green apple","canberry","mango"]
list1.sort()
print(list1) # by default it sorts alphabetically
list1.sort(reverse=True)
print(list1)

list1.sort(key=lambda x : x[1]) # sorted by second letter :P
print(list1)

# sorted
tuple1=("a","b","r","c","d","p","s")
print(sorted(tuple1))
print(tuple1)

print(sorted("huma mehadisa"))
print(sorted(list1,key=lambda x: x[2])) # based on 3rd alphabet