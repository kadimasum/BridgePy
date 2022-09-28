def sort_numbers_ascending(Arr):

    iterations = 0

    for i in range(len(Arr)):
        for j in range(len(Arr) - i - 1):
            iterations += 1
            if Arr[j] > Arr[j + 1]: 
                Arr[j], Arr[j + 1] = Arr[j + 1], Arr[j]
    return Arr

result = sort_numbers_ascending([6,2,6,1,3,24,12])
print(result)
