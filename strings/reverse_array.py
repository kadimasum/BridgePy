def reverse_array(A):
    if len(A) < 2: return A
    start = 0
    end = len(A) - 1
    while start < end:
        temp = A[end]
        A[end] = A[start]
        A[start] = temp
        start += 1
        end -= 1

    return A

print(reverse_array(['h','e','l','l','o']))