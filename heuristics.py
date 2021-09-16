from math import sqrt

# Euclidian distance
def euclidian(start, end):
    return sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2)

# Manhattan distance
def manhattan(start, end):
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

# Chebyshev distance
def chebyshev(start, end):
    return max(abs(start[0]-end[0]), abs(start[1]-end[1]))