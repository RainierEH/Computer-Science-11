# Rainier Hasbrouck
# Created 3/2/2021
# Last modified 3/2/2021
# Calculates the distance between two coordinates on a Cartesian plane.
from math import sqrt

def distance(x1, x2, y1, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(distance(0, 0, 3, 4))