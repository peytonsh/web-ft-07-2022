# Homework
## Functions

#### 1. Find the smallest number

# Write a function `smallest` that accepts a List of numbers as an argument.

# It should return the smallest number in the List.

def smallest(list):
    small = list[0]
    for i in list:
        if i < small:
            small = i
    return small

list=[3, 9, 7, 3, 6, 5, 7, 24, 6]
print(f"smallest in {list} is {smallest(list)}")


#### 2. Find the largest number

# Write a function `largest` that accepts a List of numbers as an argument.

# It should return the largest number in the List.



def largest(list):
    large = list[0]
    for i in list:
        if i > large:
            large = i
    return large
list = [3, 9, 7, 3, 6, 5, 7, 24, 6]
print(f"largest in {list} is {largest(list)}")
    

# #### 3. Find the shortest String

# Write a function `shortest` that accepts a List of Strings as an argument.

# It should return the shortest String in the List.


strList = ['good', 'bad', 'terrible']

def shortest(strList):
    small = strList[0]
    for i in strList:
        if len(i) < len(small):
            small = i
    return small

print(shortest(strList))



# #### 4. Find the longest String

# Write a function `longest` that accepts a List of Strings as an argument.

# It should return the longest String in the List.


def longest(strList):
    large = strList[0]
    for i in strList:
        if len(i) > len(large):
            large = i
    return large

print(longest(strList))
