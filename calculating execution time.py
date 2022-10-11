##to find execution time to print some word(practice)
import time
start = time.time()
for i in range( 7):
    print("UTH UK Limited")
end = time.time()
print("Execution time of the program is- ", end-start)

##practice
import datetime
start = datetime.datetime.now()
list1 = [4, 2, 3, 1, 5]
list1.sort()
end = datetime.datetime.now()
print(end-start)


##project
from time import time
start = time()
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
end = time()
execution_time = end - start