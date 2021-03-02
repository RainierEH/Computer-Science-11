import random

doors = {
    '1' : ['1', '0', '0'],
    '2' : ['0', '1', '0'],
    '3' : ['0', '0', '1']
    }

choices = ['1', '2', '3']
config = doors[random.choice(choices)]

userIn = input("Chose a door. 1, 2, or 3: ")

