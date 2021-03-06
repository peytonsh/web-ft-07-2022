# # 1. Determine the total distance travelled and the
# # total time it takes to get there by summing up
# # the total distance and the total time in the list below

# trips = [
#     { "distance": 34, "time": 10 },
#     { "distance": 90, "time": 50 },
#     { "distance": 59, "time": 25 },
#     { "distance": 83, "time": 60 },
#     { "distance": 27, "time": 15 },
#     { "distance": 68, "time": 90 }
# ]
# total = 0

# listDist = [34, 90, 59, 83, 57, 68]
# listTime = [10, 50, 25, 60, 15, 90]

# for ele in range (0, len(listDist)):
#     total = total + listDist[ele]
# print("sum of all elements in distance", total)

# total = sum(listTime)
# print("sum of time:", total)

# 2. Implement a 'pluck' function. 
# Pluck should accept a list and a string representing a 
# property name and return a list containing that property from each object.

# example
paints = [{"color": 'red', "text-align": "right"}, {"color": 'blue', "margin": "0px"}, {"color": 'yellow', "padding": "5px"}]
# pluck(paints, 'color')
# returns =>>>>> ['red', 'blue', 'yellow']

def pluck(1st,key):
    return [x,get(key) for x in 1st]
pluck(paints, 'color')