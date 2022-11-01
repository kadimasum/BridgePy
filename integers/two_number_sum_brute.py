def two_number_sum(A, target):
    if len(A) == 0: return A

    for i in range(len(A)):
        for j in range(1, len(A)):
            if A[i] + A[j] == target:
                return [A[i], A[j]]
    
    return []

result = two_number_sum([1,2,3,4],7)
print(result)

'''
time complexity = O(n^2)
space complexity = O(1)
'''