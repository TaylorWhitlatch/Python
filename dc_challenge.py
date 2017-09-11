#Declare two variables 9python dynamic)

fullName = "Taylor Whitlatch"
age = 35
myList = [];
myList.append(fullName)
myList.append(age)

print myList
def say_hello():
     print "Hello!"

say_hello()

splitName = fullName.split()
print splitName

def sayName():
    print "Hello, %s is" % splitName[0]
sayName()

import datetime
now = datetime.datetime.now()
currentYear = now.year
def myAge(yearBorn):
    print (currentYear - yearBorn)

myAge(1990)
def sum_odd_number():
    sum = 0

    for i in range(4999, 0, -2):
        sum += i

    print sum



sum_odd_number()

def sum_odd_numbers():
    i = 1
    sum = 0
    while 1
