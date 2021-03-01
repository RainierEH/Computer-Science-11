# Rainier Hasbrouck
# Created 3/1/2021
# Last modified 3/1/2021
# Simple magic 8ball

import random

responses = ['Yes',
             'Definitley',
             'Of course',
             'Probably',
             'No',
             'Probably not',
             'Don\'t count on it',
             'I don\'t think so',
             'Maybe',
             'I am not sure']

a = input('Ask a yes or no question: ')
print('You Asked:')
print(a)
print('Magic 8 Ball says:')
print(responses[random.randint(0,9)])
