#to group lists and print the list of same indices

test_list = [[10, 24,45], [48, 60, 8], [89, 37, 10]]
print("The original list is : " + str(test_list))
res = [list(x) for x in zip(*test_list)]
print("The index elements pairs list is " + str(res))

## to group the list of indices by calling map along with zip
test_list = [[1, 4, 5], [4, 6, 8], [8, 3, 10]]
print("The original list is : " + str(test_list))
res = list(map(list, zip(*test_list)))
print("The index elements pairs list is " + str(res))

###project program
inputLists = [[100, 20, 3330], [880, 550, 6], [7045, 1000, 760]]
outputLists = []
index = 0
for i in range(len(inputLists[0])):
    outputLists.append([])
    for j in range(len(inputLists)):
        outputLists[index].append(inputLists[j][ index])
    index = index + 1
a, b, c = outputLists[0], outputLists[1], outputLists[2]
print(a, b, c)