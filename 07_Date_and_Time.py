# Date time module
# Very helpful feature of python
import datetime

dir(datetime)

# Inside date time module, we have date class, time class as well as datetime (combined)
# i.e we can have date seperately, time seperately and can have both together


mybday= datetime.date(1993,3,8)

print(mybday)

print(mybday.day)
# print(mybday.time) --> # Results in error as mybday is a date object and does not have time
print(mybday.year)
print(mybday.month)

# time delta is used to add/sub certain number of days to a given date

td_object = datetime.timedelta(10000)
print(mybday+td_object)

# formatting date and time

# old method
# for formatting we use format specifiers. There are many format specifiers and
# we have to choose the ones which are required
# converting date to string

print(mybday.strftime("%A %B %d, %Y")) # format specifiers are case sensitive
print(type(mybday.strftime("%A %B %d, %Y")))
# Another method

message ="hello my bday is on {:%A %B %d, %Y}"
print(message.format(mybday))

#lets explore date time class

bday_date = datetime.date(1993,3,8)
bday_time =datetime.time(22,30,0)
bday_datetime = datetime.datetime(1989,8,19,5,0,0)

print(bday_time.second)
print(bday_datetime.microsecond)
print(bday_datetime.day)

# Todays date

now = datetime.datetime.today()
print(now)
print(now.microsecond)

#converting string to datetime object

sajan_bday="19/08/1989"
sajan_bday_date=datetime.datetime.strptime(sajan_bday,"%d/%m/%Y")
print(sajan_bday_date)
print(type(sajan_bday_date))
















