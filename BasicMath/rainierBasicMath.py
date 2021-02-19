# Rainier Hasbrouck
# Created ~ 9:00 2/19/2021
# Last Modified ~9:00 2/19/2021
# Takes user input and outputs several calculations

# try:
#     [Code]
# except ZeroDivisionError:
## this is a bit of code you can use to avoid crashing the program if a user inputs zero

# I think this print() statement is funny because I 100% overcomplicated this
print('This is a program that will do some simple math with two numbers')

userA = 0.0 # Make all these variables first so we can make them global inside
userB = 0.0 # some fuctions, to make the program easier to organize.
grabbed = 0 # The grabbed variable is made to prevent a bug where if an error is detected
            # in input, it will repeatedly call for the input again, even when a correct
            # value is chosen after.

def grabInput():
    # The reason I made grabbing an input a funtion was so it could call
    # itself when an error is detected
    global userA
    global userB
    global grabbed

    # I'm using 2 while loops here, so that the aforementioned multiple inputs bug can
    # be avoided. 
    while grabbed < 1:
        try:
            userInput = input('[1st Value] Please enter a number: ')
            userA = float(userInput)
            grabbed += 1 # Increase grabbed so that we don't try and take input for A again
        except ValueError:
            print('The number entered was an incorrect float value!')
            grabInput()
    while grabbed < 2:
        try:
            userInput = input('[2nd Value] Please enter another number: ')
            userB = float(userInput)
            grabbed += 1 # Increase grabbed so that we don't try to call grabInput() again
        except ValueError: 
            print('The number entered was an incorrect float value!')
            grabInput()
        
def doMath(type):
    # I have to declare these as global here. While I could have just made this
    # without it being a function, I started with a goal that I forgot once I was
    # half way through writing this. As I do with most of my projects ¯\_(ツ)_/¯
    global userA
    global userB
    if type == 'add':
        out = userA + userB
        # Have to format and make everything a string so we can use the +.
        # It's messy yeah, but it works, and saves me from adding seperate
        # lines to switch them all. I won't comment most of the rest
        # because it's all the same. Basically all that's happening is
        # checking if the function was called with a certain string, such as
        # add, subtrct, etc... Then we just do the math in python by assigning
        # the value to the variable 'out'
        print(str(userA) + " + " + str(userB) + " = " + str(out))
    elif type == 'subtract':
        out = userA - userB
        print(str(userA) + " - " + str(userB) + " = " + str(out))
    elif type == 'multiply':
        out = userA * userB
        print(str(userA) + " x " + str(userB) + " = " + str(out))
    elif type == 'divide':
        try:
            out = userA / userB
            print(str(userA) + " / " + str(userB) + " = " + str(out))
        # For the divide and mod functions, we check if the user has entered a 0,
        # So that we can print an error instead of crashing out the rest of the
        # program
        except ZeroDivisionError:
            print('Can\'t divide by zero!')
    elif type == 'mod':
        try:
            out = userA % userB
            print(str(userA) + " % " + str(userB) + " = " + str(out))
        except ZeroDivisionError:
            print('Can\'t divide by zero!')
    elif type == 'power':
        try:
            out = userA ** userB
            print(str(userA) + " ^ " + str(userB) + " = " + str(out))
        # I've never encountered it before, but apparently if your number is too large,
        # it won't work. Oh well, we can just catch that with this.
        except OverflowError:
            print('Could not compute the power, number entered was too large!')

# Call all the functions in order so that we can output the math we want, from
# the inputs we grabbed
grabInput()
doMath('add')
doMath('subtract')
doMath('multiply')
doMath('divide')
doMath('mod')
doMath('power')
