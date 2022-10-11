'''
Quicksort
--------
Uses divide and concour method

Pseudocode
__________
1. create function quickSort(arr):
2. Find pivort and pop it out from the array
3. declare empty left and right array
4. loop through array. append velues < pivot to left array and viceversa
5. return quickSort(find_left_array) + [pivot] + quickSort(find_right_array)
'''

def quickSort(arr):
    if len(arr) < 2: return arr
    middle = len(arr) // 2
    pivot =arr.pop(middle)
    left_array = []
    right_arr = []
    for num in arr:
        if num > pivot: right_arr.append(num)
        else:left_array.append(num)

    return quickSort(left_array) + [pivot] + quickSort(right_arr)


result = quickSort([30,7,67,4,9])
print(result)

'''
time complexity = O(n log n)
space complexity = O(n)
'''