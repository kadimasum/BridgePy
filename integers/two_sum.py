def twoSum(nums, target):
    if len(nums) < 2: return [-1, -1]
    for i in range(len(nums)):
        j = i + 1
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    
    return [-1, -1]

result = twoSum([2,3,5,7,9], 16)

print(result)

'''
PSEUDOCODE
-----------
1. Create a function twoSum(nums, target)
2. Check if len(nums) < 2 return [-1, -1]
3. Loop through nums to find two numbers that add up to target
4. return the indices of the numbers
5. If numbers do not exist return [-1, -1]

* Time complexity = O(n^2)
* Space complexity = O(n)
'''