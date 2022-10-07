'''
Question
--------------
Suppose you have a sorted list of 128 names, and you’re searching
through it using binary search. What’s the maximum number of
steps it would take?

Pseudocode
__________
1. Write a function max_steps(no_of_names):
2. create a variable steps = 0
3. start = 0
4. Loop
5. while start < no_of_names: midpoint = no_of_names // 2, steps + 1, start = midpoint + 1
6. return steps
'''

def max_steps(number_of_names):
    steps = 0
    start = 0

    while  start < number_of_names:
        midpoint = (start + number_of_names) // 2    
        steps += 1
        start = midpoint + 1

    return steps

print(max_steps(128))
        

'''
Time complexity = O(n)
Space complexity = O(1)
'''
