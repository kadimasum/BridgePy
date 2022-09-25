
'''
3 factorial = 3 * 2 * 1

PSEUDOCODE
-----------
1. write a function iterative_factorial(n)
2. Iniitialiaze factorial to 1
3. Loop within the range of n+1 
4. return the product of factorial and all iterative numbers
'''
def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

print(iterative_factorial(3))

'''
* Time complexity = O(n)
* Space complexity = O(1)
'''