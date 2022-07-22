


#1. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"])

# x = ["Elie", "Tim", "Matt"]
# for list in x:
#     print(list[0])
   
# n_list = []  #option 2
# for i in list:
#     n_list.append(i[0])

# #2. Print out the numbers 1-10 from the list below
# nums = [
#     {"num": 1},
#     {"num": 2},
#     {"num": 3},
#     {"num": 4},
#     {"num": 5},
#     {"num": 6},
#     {"num": 7},
#     {"num": 8},
#     {"num": 9},
#     {"num": 10},]

# for i in nums:
#     print(i["num"])

# print(nums["num"])
#3. Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

abbreviations = ["CA", "NJ", "RI"] 
state_names = ["California", "New Jersey", "Rhode Island"]

new_dict = {}


for i in range(len(abbreviations)):
    new_dict[abbreviations[i]] = state_names[i]
    
    print(new_dict)
    
#4. see colorsProblems.py