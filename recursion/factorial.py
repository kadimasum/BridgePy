
'''
3 factorial =  3 * 2 * 1

Pseudocode
------------
1. Write fun recur_fuctorial(n)
2. if n == 1 return n
3. else return n * recur_fuctorial(n - 1)
'''
def recur_factorial(n):
    if n == 1: return n
    else: return n * recur_factorial(n - 1)

print(recur_factorial(4))


'''
* Time complexity = O(n)
* Space complexity = O(n)
'''