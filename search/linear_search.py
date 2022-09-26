def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

result = search([2,4,3,8,5], 8)
print(result)