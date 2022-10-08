#my practice to find mean of goven set of numbersz
import statistics

data = [18,88,45,43,25,75,88,20,16,8,15,61,451,125896,10]

x = statistics.mean(data)
print(x)
#practicing to find mean median mode

import statistics

data = [11, 21, 11, 19, 46, 21, 19, 29, 21, 18, 3, 11, 11]

x = statistics.mean(data)
print(x)

y = statistics.median(data)
print(y)

z = statistics.mode(data)
print(z)

a = statistics.stdev(data)
print(a)
#python project
# Median
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)
