def can_sum(target_number, numbers):
    memo = set()
    for num in numbers:
        complement = target_number - num
        if complement in memo:
            return True
        memo.add(num)
    return False

print(can_sum(6, [2,3,5,4]))

'''
Time complexity = O(n)
Space complexity = O(n)
'''
