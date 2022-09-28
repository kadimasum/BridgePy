def binary_recur(arr, start, end, target):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            return binary_recur(arr, mid + 1, end, target)
        else:
            return binary_recur(arr, start, mid - 1, target)
    else: return -1


arr1 = [6,4,5,8,3]
result = binary_recur(arr1, 0, len(arr1) - 1, 6)
print(result)
        