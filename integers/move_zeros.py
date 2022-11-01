'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 https://leetcode.com/problems/move-zeroes/

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

'''


def move_zeros(nums):
    prev = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[prev]
            nums[prev] = nums[i]
            nums[i] = temp
            prev += 1

    return nums

print(move_zeros([0,1,0,3,12]))

'''
Space complexity = O(1)
Time complexity = O(n)
'''