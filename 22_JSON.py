
"""
Lets Learn about json in python

"""
"""
We have the following methods :

Load
Loads - load json from string
dump 
dumps  - sump string to json
"""

import json

file = open("readfile.txt",'r',encoding="utf-8")
jsonvalue = json.load(file) # Here it converts json to dictionary
# jsonval = json.load(file) # loading can be done only once : REASON UNKNOWN
print(jsonvalue)

Stringvalue = """
{"name":"mehadi",
"age": 25,
"married": true
}
"""
jsonvalue1 = json.loads(Stringvalue)

print(jsonvalue1)

file1 = open("writingfile.txt",'w',encoding = "utf-8")
dict1 = {}
dict1['name'] = "huma~~"
dict1['age'] = 25
dict1 ['married'] = True
dict1['cars'] = None

json.dump(dict1,file1,ensure_ascii=False)



print(jsonvalue)
print(type(jsonvalue))
str = json.dumps(jsonvalue,ensure_ascii=False)
print(str)