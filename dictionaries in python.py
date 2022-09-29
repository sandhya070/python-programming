# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'where there is a will', 2: 'there is ', 3: 'a way'})
print("Dictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'shallu'), (2, 'shashu')])
print("Dictionary with each item as a pair: ")
print(Dict)

#printing an employment data by using dictionary
Employee = {"Name": "shreyank", "Age": 23, "salary":25000,"Company":"UTH"}
print(type(Employee))
print("printing Employee data .... ")
print("Name : %s" %Employee["Name"])
print("Age : %d" %Employee["Age"])
print("Salary : %d" %Employee["salary"])
print("Company : %s" %Employee["Company"])

#to show repetation in tupples
tuple_ = ('UTH ', "NAGARBHAVI")
print("Original tuple is: ", tuple_)
tuple_ = tuple_ * 5
print("New tuple is: ", tuple_)
