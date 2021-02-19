# Rainier Hasbrouck
# Created ~ 9:00 2/19/2021
# Last Modified ~9:00 2/19/2021
# Takes user input and outputs several calculations

# try:
#     [Code]
# except ZeroDivisionError:
## this is a bit of code you can use to avoid crashing the program if a user inputs zero

userInput = input('Please enter a number: ')
userA = float(userInput)
userInput = input('Please enter another number: ')
userB = float(userInput)

def doMath(type):
    if type == 'add':
        out = userA + userB
        print(str(userA) + " + " + str(userB) + " = " + str(out))
    elif type == 'subtract':
        out = userA - userB
        print(str(userA) + " - " + str(userB) + " = " + str(out))

doMath('add')
doMath('subtract')
