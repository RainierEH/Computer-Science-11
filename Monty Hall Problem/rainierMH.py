import random

doors = {
    '1' : ['1', '0', '0'],
    '2' : ['0', '1', '0'],
    '3' : ['0', '0', '1']
    }

choices = ['1', '2', '3']
config = random.choice(choices)

print(doors[config])
print(config)

userIn = int(input("Chose a door. 1, 2, or 3: "))

userDoor = doors[config[userIn]]
