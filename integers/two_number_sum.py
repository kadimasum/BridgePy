'''
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.



input: 

array = [3,5,-4,8,11,1,-1,6]

targetSum = 10



output:

[-1,11]






def twoNumberSum(array, targetSum):

     // write code here


'''

def twoNumberSum(A, target):
    if len(A) == 0: return A
    map = {}
    for i in range(len(A)):
        complement = target - A[i]
        if complement in map:
            return [complement, A[i]]
        map[A[i]] = i

    return []

result = twoNumberSum([2,4,6,7], 9)
print(result)

'''
Time complexity = O(n)
Space complexity = O(n)
'''