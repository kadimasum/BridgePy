'''
Write a function f(n) that returns that returns the first n values of the fibonacci sequence
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''
def fibonacci(n):
    if n == 1: return 1
    elif  n == 2: return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


result = fibonacci(10)
print(result)