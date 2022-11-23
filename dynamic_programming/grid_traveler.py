'''
Say that you are a traveller on a 2D grid. You begin in the top left corner and your goal is to travel to the bottom right corner. You may only move bottom or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?

Write a function 'gridTraveller(m, n)' that calculates this.
'''

def gridTraveller(m, n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return gridTraveller(m - 1, n) + gridTraveller(m, n - 1)

print(gridTraveller(1,1))
print(gridTraveller(0,0))
print(gridTraveller(2,3))
print(gridTraveller(3,2))
print(gridTraveller(3,3))
# print(gridTraveller(80,80)) his line takes too long to execute


'''
Time complexity = O(2 ^ (n + m))
Space complexity = O(n + m)
'''