# to remove duplicate items from the list
import mydata as mydata

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

# to print the length of the list
test_list = [1, 4, 5, 7, 8]
print("The list is : " + str(test_list))
counter = 0
for i in test_list:
    counter = counter + 1
print("Length of list using naive method is : " + str(counter))

# import module
from tabulate import tabulate
mydata = [
    ['a', 'b', 'c'],
    [12, 34, 56],
    ['Geeks', 'for', 'geeks!']
]
print(tabulate(mydata))

#to print the odd numbers present in tupple
tuple_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)
for value in tuple_:
    if value % 2 != 0:
        print(value)
    else:
        print("These are the odd numbers present in the tuple")


