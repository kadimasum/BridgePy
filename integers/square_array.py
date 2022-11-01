'''
# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order. 



For example:



      array = [1,  2,  3,  5,  6,  8,  9] 



Returns:

[1,  4,  9,  25,  36,  64,  81]

def sortedSquareArray(array):     

      # Write your code here.
'''

def square_array(A):
    if len(A) == 0: return A
    for i in range(len(A)):
        A[i] = A[i] * A[i]

    return A

result = square_array([1,2,3,4,5])
print(result)

'''
Space complexity = O(1)
Time complexity = O(n)
'''