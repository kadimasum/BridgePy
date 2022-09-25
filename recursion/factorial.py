
'''
3 factorial =  3 * 2 * 1

Pseudocode
------------
1. Write fun recur_fuctorial(n)
2. if n == 1 return n
3. else Call recur_fuctorial(n - 1) and store it in a temp variable
4. return temp *= n
'''
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n - 1)
        temp *= n
        return temp

print(recur_factorial(4))


'''
* Time complexity = O(n)
* Space complexity = O(n)
'''