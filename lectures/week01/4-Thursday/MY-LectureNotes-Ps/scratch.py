# Homework
## Iterative Programming

#### 1. Multiply Vectors

# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:


# nums = [2, 4, 5] 
# num1 = [2, 3, 6] 

# products = []

# for x1, x2 in zip(nums, num1):
#     products.append(x1 * x2)
    
# print(products)


# #### 2. Matrix Addition

# # Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:


# list1 = [2, -2]
# list2 = [5, 3] 
# product = []

# for x1, x2 in zip(list1, list2):
#     product.append(x1 + x2)
    
# print(product)
    


# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add


# 1 3
# 2 4

# and


# 5 2
# 1 0


# results in0

# 6 5
# 3 4


# x = [[1, 3],
#     [2,4]]

# y = [[5,2],
#     [3,4]]

# result = [[0,0],
#           [0,0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         for j in range(len(x[0])):
#             result[i][j] = y[i][j] + x[i][j]

# for r in result:
#     print(r)           

# #### 3. Matrix Addition II

# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.

# #### 4. De-dup

# Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

# #### 5. Leetspeak

# Given a paragraph of text as a String, print the paragraph in [leetspeak](https://en.wikipedia.org/wiki/Leet). 

# To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# | Letter | Translates To |
# |:------:|:-------------:|
# | A      | 4             |
# | E      | 3             |
# | G      | 6             |
# | I      | 1             |
# | O      | 0             |
# | S      | 5             |
# | T      | 7             |

# Example: If your program is given the String `"I am a leet programmer"`, it should print `"1 4m 4 l337 pr0gr4mm3r"` as the leetspeak translation

# #### 6. Long-long Vowels

# Given a word as a string, print the result of extending any long vowels to the length of 5. 

# Examples:

0

# Good => Goooood 
# Cheese => Cheeeeese 
# Man => Man 
# Spoon => Spooooon 
0

word = 'spoon'

word = word.replace('ee', 'eeeee')
word = word.rep
#### 7. Caesar Cipher

# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? [Learn about it here](http://practicalcryptography.com/ciphers/caesar-cipher/).

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"


## Large 

### Matrix Multiplication
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix.

# How do you multiple two matrices?

