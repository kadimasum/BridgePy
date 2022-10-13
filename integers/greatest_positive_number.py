# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    if len(A) == 0: return 0
    greatest_positive = A[0]
    for i in range(len(A)):
        if A[i] > greatest_positive:
            greatest_positive = A[i]

    if greatest_positive < 1: return 1
    
    for i in range(greatest_positive):
        if i not in A: 
            greatest_positive = i
        else: greatest_positive += 1
    
    return greatest_positive
        


 
result = solution([1,2,4])
print(result)