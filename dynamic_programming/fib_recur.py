'''
Write a function 'fib(n)' that takes in an argument. The function should return the nth number of the fibonacci sequence
1,1,2,3,5,8
'''

def fib(n):
    if n == 1 or n == 2: return 1
    if n == 0: return 0
    return fib(n - 1) + fib(n - 2)
  

result = fib(6)
print(result)
    