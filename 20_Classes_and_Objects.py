# Lets learn about classes in python
import datetime
class User:
    pass # just so that class will have a line. Have no use

user = User()
user.name = "huma"
print(user.name)

user2 = User()
user2.age = 21

print(user2.age)

#print(user2.name) # gives an attribute error as the field "name" is not defined for user2

# Then why do we use classes if the blue print is not available
# lets check out

class Student:
    # This is the initialization method for the instances of Student class
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    # lets define other function which returns the age
    def give_age(self):
        today = datetime.datetime.today()
        birthday_date = datetime.datetime.strptime(self.birthday, "%Y%m%d")
        print(birthday_date)
        print(today)
        days = (today-birthday_date).days
        print(days)
        print(days/365)
        return (days/365)




st1 = Student("Mehadisa","19930308") # birthday in yyyymmdd format


print(st1.name)

exact_age = st1.give_age()

print("exact age of ",st1.name,"is",exact_age)

