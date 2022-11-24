'''
Write a function 'how_sum(target_sum, numbers)' that takes in a target sum and an array of numbers as arguments. The function should return an array containing any combination of elements that add up to exactly the target sum. If there is no combination that adds up to the target sum the function should return null.

If there are multiple combinaions possible you may return any single one
'''
def how_sum(target_sum, numbers):
    result = []
    for i in range(len(numbers) - 1):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                result.append(numbers[i])
                result.append(numbers[j])
                return result
        
    return None

print(how_sum(9, [2,5,4,3]))

'''
Time complexity = O(n^2)
Space complexity = O(1)
'''