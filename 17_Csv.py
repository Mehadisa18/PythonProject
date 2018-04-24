# To read/ write data into csv..
# lets try without csv module.

path ="NewGoogle Stock Market Data.csv"
file = open(path)
data = [line for line in file]
print(data[0])
print(data[1])

line = data[1]

print(type(line[0])) # here every value is in the form of a string
print(line[0]) # still not comma seperated 

# lets strip this off any newline characters

ourdata =line.strip().split(',')

print(ourdata[0]) # now it is comma seperated.

# how ever if the strings contain any commas, it will be a problem
# hence we use csv module from python

import csv

file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)
k = next(reader)
#data = [row for row in reader]
#print(data[0])
#data1 = [row for row in reader]
#print(data1[0])

# In order to convert them, we use the following method


reader2 = csv.reader(file)
#header1 = next(reader2)
newdata =[]
import datetime
for row in reader2:
    date = datetime.datetime.strptime(row[0],"%M/%d/%Y")
    #print(date)
   # print(type(date))
    low_value = float(row[1])
   # likewise we can convert all the values
    newdata.append([date,low_value])
   


   # for writing
file2 = open('csvwriting.csv','w')
writer = csv.writer(file2)
writer.writerow(["date","value"])

for row in newdata:
    writer.writerow([row[0].strftime("%d/%M/%Y"),row[1]])





















