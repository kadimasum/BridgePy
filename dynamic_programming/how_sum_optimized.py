def how_sum(target_sum, numbers):
    result = []
    target_num_set = set()
    for num in numbers:
        complement = target_sum - num
        if complement in target_num_set:
            result.append(num)
            result.append(complement)
            return result
        target_num_set.add(num)
    return None

print(how_sum(7, [6,3,4]))