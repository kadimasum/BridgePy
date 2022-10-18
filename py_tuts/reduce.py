from functools import reduce


nums = [3,5,2,5,2,8]

result = reduce(lambda a, b: a + b, nums)
print(result)