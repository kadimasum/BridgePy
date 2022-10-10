'''
Given an array of numbers, find the sum of all elements recursively

Pseudocode
_____________
1. Create a function findSum(arr):
2. return 0 if arr is empty
3. sum = arr[0]
4. return sum + findSum(arr[1:])

'''

def findSum(arr):
    if len(arr) == 0: return 0
    sum = arr[0]
    return sum + findSum(arr[1:])

result = findSum([1,2,4,-1,0,5])
print(result)

'''
Time complexity = O(n)
Space complexity = O(n)
'''
