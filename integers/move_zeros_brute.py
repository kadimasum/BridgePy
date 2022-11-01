'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]


'''

def move_zeroes(nums):
    if nums[0] == 0 and len(nums) == 1: return nums

    new_array = []

    for i in nums:
        if i != 0:
            new_array.append(i)

    for i in range(len(new_array), len(nums)):
        new_array.append(0)

    return new_array


print(move_zeroes([0,1,0,3,12]))