def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid


    return -1

arr = [6,4,5,8,3]
result = binary_itr(arr, 0, len(arr), 5)
print(result)