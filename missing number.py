#to find missing number by ussing array and if else statement
arr = [1,2,3,4,5,6,7,9,10]
missing_elements = []
for ele in range(arr[0], arr[-1]+1):
    if ele not in arr:
        missing_elements.append(ele)
print(missing_elements)

#
arr = []
n = int(input("enter size of array : "))
for x in range(n-1):
    x=int(input("enter element of array : "))
    arr.append(x)
sum = (n*(n+1))/2;
sumArr = 0
for i in range(n-1):
    sumArr = sumArr+arr[i];
print(int(sum-sumArr))

##project practiced and writen code
def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output


listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))