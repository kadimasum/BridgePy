'''
PROBLEM Given an unsorted list of integers, write a function that returns a
new list with all duplicate values removed.
'''

def remove_duplicates(A):
    my_set = set()
    arr = []
    for i in range(len(A)):
        if A[i] not in my_set:
            my_set.add(A[i])
            arr.append(A[i])     

    return arr

result = remove_duplicates([2,5,2,4,2,6,1,1])
print(result)