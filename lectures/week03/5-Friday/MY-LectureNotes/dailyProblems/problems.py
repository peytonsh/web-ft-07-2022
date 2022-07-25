# Return a new list with each element multiplied by 5

# let 
from subprocess import list2cmdline


nums = [56, 34, 34, 1, 1, 1, 23, 12, 89, 89, 89, 70, 56] 

index = []
for x in nums:
    index.append(x * 5)
print(index)


# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).

list1 = ("job", "Elie") 
list2 = ("Instructor", "name")

new_dict = {}

for i in range(len(list1)):
    new_dict[list2[i]] = [list1[i]]
    
print(new_dict)