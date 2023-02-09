'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

https://leetcode.com/problems/3sum/

[2,-2,0]


Pseudocode
___________

First iteration
-----------
outer loop -> 2 [i = 0]
inner loop -> -2 [j = 1]
middle loop -> 0 [k = 2]

Second iteration
-----------
outer loop -> -2 [i = 1]
inner loop -> 0 [j = 1]


'''

def threeSum(nums):
    result = []
    nums = sorted(nums)
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    
    return result
print(threeSum([2,-2,0,4,-2]))

    

