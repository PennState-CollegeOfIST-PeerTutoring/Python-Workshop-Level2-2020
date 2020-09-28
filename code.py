############Functions############
average = 0
number = 0
needNumbers = True
counter = 0
while needNumbers:
    number = int(input("Enter a number for average, enter -1 to stop: "))
    if number == -1:
        needNumbers = False
        break
    average = average + number
    counter += 1
average /= counter
print("Average is " + str(average))

#################################
def calc_Average(prompt):
    average = 0
    number = 0
    needNumbers = True
    counter = 0
    while needNumbers:
        number = int(input(prompt + ", enter -1 to stop: "))
        if number == -1:
            needNumbers = False
            break
        average = average + number
        counter += 1
    average /= counter
    return average

print(calc_Average("Enter a number"))
calc_Average("Enter a GPA")
calc_Average("Enter a Price of a home")
calc_Average("Enter the fastest speeds")

def calc_salesTax(priceOfItem, salesTax):
	finalCost = priceOfItem * (1 + salesTax)
	return finalCost

print(calc_salesTax(25.00, .06))

#Break#
i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

#Continue#
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)

#Default Parameter#

def my_function(name = 'User'):
	print('Hello there, ' + name + '!')

my_function('Jimmy')
my_function('Cole')
my_function()



#################################

#########Classes/Objects#########

#Creating a Class#
class MyClass:
	x = 5
class Person:
	name = 'Steve'
	height = 72 #inches
	genderMale = True
	hair = False

#Creating an Object#

person1 = Person()
print(person1.name)
print(person1.height)
print(person1.genderMale)
print(person1.hair)

#Constructors#

class OldPerson:
	def __init__(self, name, height, genderMale, hair, age):
		self.name = name
		self.height = height
		self.genderMale = genderMale
		self.hair = hair
		self.age = age
    
    def getInfor(self):
    	print('This person’s name is: ' + self.name + '.  They are ' + self.height + 'inches tall.  They are ' + self.age + ' years old')

    def sayHello(self):
    	print('Why hello there, my name is ' + self.name + ', it is a pleasure speaking with you tonight!')

person2 = OldPerson('Jordan', 70, True, True, 21)

person2.getInfo
person2.sayHello

#Modifying Properties and Objects#
person2.age = int(input("How old are you? "))
hair = input("Do you have hair? ")
if hair == 'yes':
    person2.hair = True
else:
    person2.hair = False
print(person2.hair)


#######Exception Handeling#######
x = 7

try:
	print(x)
except:
	print('An Exception Occurred')

#Finally#
try:
	print(y)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
finally:
	print('The ‘try except’ is finished')

#Raise Exception"
age = int(input('How old are you?'))
if age < 0:
	raise Exception('Sorry, no numbers below zero')
