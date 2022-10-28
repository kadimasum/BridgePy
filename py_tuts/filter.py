'''
Given an array of numbers. Find if a given number exists
'''
nums = [3,5,2,5,2,8]

result = list(filter(lambda n: n == 2, nums))
print(result)