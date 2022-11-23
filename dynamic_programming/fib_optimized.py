'''
Memoization - Use an object: Keys will be arguments to the function, values will be the return value
'''

def fib(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print(fib(5))
print(fib(8))
print(fib(9))
print(fib(50))

'''
Time complexity = O(n)
Space complexity = O(n)
'''