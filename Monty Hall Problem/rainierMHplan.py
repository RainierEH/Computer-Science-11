# Rainier Hasbrouck
# Created 3/1/2021
# Last modified 3/1/2021
# Pseudocode for the Monty Hall problem. This stuff hurts my brain :P

doors = {
    '1' : ['1', '0', '0']
    '2' : ['0', '1', '0']
    '3' : ['0', '0', '1']
    }

Make a dictionary "doors" containing lists with possible door configurations

Select a random configuration from the dictionary

Ask the user to pick a door

If the door is a goat, reveal the location of the other goat
Otherwise, if the door is the car, pick any goat to reveal

Ask the user if they would like to switch the door

Reveal the car location, and tell the user what they picked.
