# dictionaries are like maps
# They have key value pairs
import datetime
User = { "name":"Huma Mehadisa",
          "age": 25,
          "time": datetime.datetime(2017,3,29,00,00,00).strftime("%Y,%m,%d") }
print(User)

print(User["name"])

NewUser = dict(name="Sajan",age=25, time=datetime.datetime(2017,3,29).strftime("%Y"))

print(NewUser)

NewUser["Languages_known"]="english"

print(NewUser)

#print(NewUser["languages_known"]) # error : keys are case sensitive

#print("hello") ## The interpreter stops at the error

if 'location' in NewUser:
    print("hello")
else:
    print("bye")

# try catch 

try:
    print(NewUser["location"])
except Exception:   # Here u can mention specific exception name like keyerror
     print("bad key ")

# get from the dictionary

print(NewUser.get('location',0)) # here 0 represents default value which will get returned
                                 # if 'location' key is not present

# Iteration over a dictionary

for k in NewUser.keys():
    print(NewUser[k])
    print(k,"=",NewUser[k])

for k, v in NewUser.items():
    print(k,"=",v)

print(NewUser.pop('location','No key found')) # pop is used to remove a key and
                                              # return its corresponding value
                                              # If key is not found then the default value mentioned
                                              # will be returned
print(NewUser.pop("name","0"))
print(NewUser)

print(NewUser.popitem()) # removes some item and returns its key value pair


#default dict
# sets initial value inside a dictionary
from collections import defaultdict
dict1 = defaultdict(list)
dict1[0].append("k")
print(dict1)





