def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
            A[i + 1] = key
    return A
result = insert_sort([6,2,6,1,3,24,12])
print(result)
    