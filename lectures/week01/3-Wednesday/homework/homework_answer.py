total_bill = float(input("what is the total bill amount?>>"))
level_of_service = input("how would you rate your service? Good, fair, bad>>")

good_service = 0.2
fair_service = 0.15
bad_service = 0.1

if level_of_service == "good":
    tip = total_bill * good_service
elif level_of_service == "fair":
    tip = total_bill * fair_service
else :
    tip = total_bill * bad_service

#total bill = tota_bull + TIp
print(f"tip is ${tip}0") #print(f"tip is %.2f" %tip)
print(f"your bill is ${total_bill + tip}0") #print(f"your bill is %.2f" % total bill)











total_bill = float(input("what is the total bill amount?"))
level_of_service = input("how would you rate your service? Good, fair, bad")

good_service = 0.2
fair_service = 0.15
bad_service = 0.1

if level_of_service == "good":
    tip = total_bill * good_service
elif level_of_service == "fair":
    tip = total_bill * fair_service
else :
    tip = total_bill * bad_service

split_bill = int(input('split bill how many ways?'))


print(f"tip is ${tip}0")
print(f"your bill is ${total_bill + tip}0")
print(f"The bill is split {split_bill} ways")
print(f"total amount per a person ${(total_bill + tip) / split_bill}0")










amount_of_coins = input('how many coins do you have?')

if amount_of_coins == 0:
    Print("do you want another coin?")
elif yes:
    print("You have 1 coins")


#Problem 3

coin_tally=0
print("you have 0 coins")

give_coin = inout("would you like a coin?")

while give _coin == "yes":
    coin_tally += 1
    print(f"you have {coin_tally} coins")
give_coin = input("do you want another?")

else:
    print("bye")
    
    
#problem 4

width = input("width? ")
width = int(width)

height = input("height? ")
height = int(height)

print("*"*width)

while (height-2 > 0): #-2 after height will make the height of the stars 5
    print("*" + " " * (width-2) + "*")
    height -=1
    
print("*"*width)







#problem 5

height = int(input("What is the height? "))

i = 0
while i < height:
    # print((height - 1) * " " + "*" * (2(i + 1)- 1) + (height - 1) * " ")
    # print((height - i) * ' ' + (1 + 2*i) * '*' + (height - i) * ' ')
    print((height - i) * " " + (2 * (i + 1) - 1) * "*" + (height - i) * " ")
    i +=1