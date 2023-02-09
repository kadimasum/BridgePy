
def kth_smallest(arr, k):
    arr = sorted(arr)
    new_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            new_arr.append([arr[i], arr[j]])

    return new_arr[k]

print(kth_smallest([1,2,3], 2))