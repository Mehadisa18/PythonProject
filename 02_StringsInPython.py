message1 = "Hello this is a string with double quotes"
message2 = 'Hello this is string with single quotes'
message3="Hello this is a string where there are 'single quotes' with in double quotes"
message4='Hello this is a string where there are "double quotes" with in single quotes'
message5='Here I\'m escaping the aposthrophe with a back slash'
message6=""" here is a sentence which contains both 'single' and "double quotes" """
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message1[1])
# help(str)
str1="hello"
str2="hellor"
print(str1 in str2)