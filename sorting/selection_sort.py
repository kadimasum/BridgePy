
'''
selection sort - find the smallest item in the array, pop it and add it to a new array. Repeat the process and return the new array

Pseudocode
______________
1. Create a function sortArray(arr):
2. if len(arr) < 2 return arr
3. Create new_arr = []
4. Loop- find smallest index
5. Append smallest to new array
6. return new_arr

'''

def selectionSort(arr):
    if len(arr) < 2: return arr
    sorted_array_ascending = []
    for i in range(len(arr)):
        smallest = arr[0]
        smallest_index = 0
        for j in range(1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        sorted_array_ascending.append(arr.pop(smallest_index))
    
    return sorted_array_ascending


result = selectionSort([9,5,23,4, -1, 0])
print(result)

'''
Time complexity = O(n^2)
Space complexity = O(n)
'''