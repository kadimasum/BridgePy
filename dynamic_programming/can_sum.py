'''
write a function can_sum(target_sum, numbers) that takes in a target sum and an array of numbers as arguments.

The function has to return a boolean indicating weather or not it is possible to generate the target sum using numbers from the array

You may use an element of an array as many times as needed.

You may assume that all inputs are non negative
'''

def can_sum(target_sum, numbers):
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum: 
                return True
        return False

print(can_sum(4, [2,3,5,2]))
'''
Time complexity = O(n^2)
Space complexity = O(1)
'''