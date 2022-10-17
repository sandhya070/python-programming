##code 1
item1="stearing cover"
item2="break pads"
item3="engine oil"
item4="clutch wire"
items=["stearing cover","break pads","engine oil","clutch wire"]
print(items)
print(items[2])
print("the third item in the itesm list is:",item2)
items= print(item2)

##code2
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

#code3
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

