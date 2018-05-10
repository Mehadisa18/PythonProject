"""
Two methods to read a text file 

f= open("file name ") 

with open("filename") as f:

"""

f = open("textfile1.txt") # if the file doesnt exist, it throws an error
k=f.read()
f.close()
print(k)

# if we open it in write mode, the file gets created automatically
t = open("textfile2.txt","w")
t.write("huma")
t.close() # we have to close it compulsarily or else the memory will be at stake

t1 = open ("textfile2.txt")
print("*** ",t1.read())
t1.close()


# second method
# if we use with keyword then we need not close the file.
# python itself takes care of it

with open("textfile2.txt") as f:
    print(f.read())

with open("textfile1.txt","w") as f1:
    for i in range(1,11):
        f1.write(str(i)) # takes only strings
    
#print(f.read()) # operation on closed file


with open("textfile1.txt") as f:
    print(f.read())
#print(f.read())#operation on closed file


with open("textfile1.txt","a") as f:
    for i in range(11,21):
        print(i, file=f) # another way to write

with open("textfile1.txt") as g:
    print(g.read())    

try:
 with open("textfile3.txt") as h:
     text=h.read()
except:
    text=None

print(text)

   
    



