# use of class
class computer:
    def config(self):
        print("i3, 8gb, 1tb")


com1 = computer()
com2 = computer()
computer.config(com1)
computer.config(com2)


# use of object in cass
class car:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname, self.year)


c1 = car("Swift Dezire", 2014)
c1.display()


# single level inheritance
class A:
    def feature1(self):
        print("feature 1 of computer is normal")

    def feature2(self):
        print("feature 2 of computer is normal")


a1 = A()
a1.feature1()
a1.feature2()


class b(A):
    def feature3(self):
        print("feature 3 of computer is normal")

    def feature4(self):
        print("feature 4of computer is normal")


b1 = b()
b1.feature2()
b1.feature4()


# multi level inheritance
class A:
    def feature1(self):
        print("feature 1 of computer is normal")

    def feature2(self):
        print("feature 2 of computer is normal")


a1 = A()
a1.feature1()
a1.feature2()


class b(A):
    def feature3(self):
        print("feature 3 of computer is normal")

    def feature4(self):
        print("feature 4of computer is normal")


class c(b):
    def feature5(self):
        print("feture 5 of computer is normal")


b1 = b()
b1.feature2()
b1.feature4()
c1 = c()
c1.feature5()
c1.feature2()


# multiple level inheritance
class A:
    def feature1(self):
        print("feature 1 of computer is normal")

    def feature2(self):
        print("feature 2 of computer is normal")


a1 = A()
a1.feature1()
a1.feature2()


class b(A):
    def feature3(self):
        print("feature 3 of computer is normal")

    def feature4(self):
        print("feature 4of computer is normal")


class c(b, A):
    def feature5(self):
        print("feture 5 of computer is normal")


b1 = b()
b1.feature2()
b1.feature4()
c1 = c()
c1.feature5()
c1.feature2()
c1.feature5()
c1.feature3()


##polymorpism
class Duck:

    def __init__(self, name):
        self.name = name

    def quack(self):
        print('Quack!')


class Car:

    def __init__(self, model):
        self.model = model

    def quack(self):
        print('I can quack, too!')


##
# Python program to demonstrate
# duck typing


class Bird:
	def fly(self):
		print("fly with wings")

class Airplane:
	def fly(self):
		print("fly with fuel")

class Fish:
	def swim(self):
		print("fish swim in sea")

# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
	obj.fly()

