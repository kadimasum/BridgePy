'''
Write a function:
function solution(A);
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def smallest_positive_in_array(A):
    my_set = set()
    greatest_positive = A[0]
    for i in A:
        if i > 0:
            my_set.add(i)
        if i > greatest_positive:
            greatest_positive = i


    for i in range(1, len(A) + 1):
        if i not in my_set:
            return i

    if greatest_positive < 0: return 1
    else: return greatest_positive + 1



result = smallest_positive_in_array( [1, 3, 6, 4, 1, 2])
print(result)