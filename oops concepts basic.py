import temp as temp


class car:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname, self.year)


c1 = car("Swift dezire", 2014)
c1.display()

#to print employee detail by using class in oops concept
class Bird:
    def speak(self):
        print("Bird speak")
#child class Dog inherits the base class Animal
class Dog(Bird):
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()

#encaptulation coding

class Employee:
 def __init__(self, name, age):
        self.name = name
        self.__age = age


def display(self):
            print(self.name)
            print(self.age)
emp = Employee('shreyank', 23)
#print(temp.name)
print(emp._Employee__age)

#polymorphism
a = 90
b = 10
print(a + d)
c = "Shallu"
print(c + d)
##
# Initializing a dictionary with some elements
Dictionary = {1: 'Java', 2: 'Python', 3: 'Dictionary'}
print("\nDictionary created using curly braces: ")
print(Dictionary)
# Creating a Dictionary with keys of different data types
Dictionary = {'Website': 'Java', 3: [2, 3, 5, 'Dictionary']}
print("\nDictionary with keys of multiple data type: ")
print(Dictionary)
