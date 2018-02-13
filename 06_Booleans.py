# lets check booleans

a = True
b= False

# TRUE AND FALSE WITH OUT CAPITAL T AND F ARE NOT ACCEPTED

print(bool(34)) # bool of any value apart from 0 gives true (even -ve)
print(bool(0))  # This gives false

print(bool(" ")) # bool of any string gives true
print(bool("") )# bool of empty string gives false

# bool to other data types

print(str(True))
print(int(False))

# Arithmatic using bools

a = 3+True
b = 3- False
print (a)
print (b)        