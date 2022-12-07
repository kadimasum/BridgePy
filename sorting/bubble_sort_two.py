def sort_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr) ):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr
print(sort_arr([5,3,6,3,9,2]))