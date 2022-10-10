
def smallest_int_position(arr):
    if len(arr) < 1: return -1
    smallest_int = arr[0]
    int_position = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_int:
            smallest_int = arr[i]
            int_position = i

    return int_position

result = smallest_int_position([9,67,20,5])
print(result)