# Rainier Hasbrouck
# Created 3/1/2021
# Last modified 3/1/2021
# Tells you your grade based on a percentage you input

done = 1

while done > 0
  try:
    score = input("Enter your score here: ")
    outOf = input("What was the test out of? ")
  
    percentage = score / outOf
    if percentage < 0 or percentage > 100
      print("Your percentage was: " + str(percentage))
      done -= 1
    else:
      print("Test score was either above 100, or under 0. Check values and enter again.")
  except ZeroDivisionError:
    print("Test score can't be out of 0!")
    
def findGrade(score):
  if score >= 86:
    print('Your grade was: A')
    print('Good job, keep it up!')
  elif score >= 73 and score <= 85:
    print('Your grade was: B')
    print('Great! Keep trying your best!')
  elif score >= 67 and score <= 72:
    print('Your grade was: C+')
    print('You\'re getting there, keep it up!')
  elif score >= 60 and score <= 66:
    print('Your grade was: C')
    print('Get working, you\'ll get there!')
  elif score >= 50 and score <= 59:
    print('Your grade was: C-')
    print('You can do better!')
  else:
    print('Your grade was: F')
    print('Better luck next time!')
