'''
Write a funtion that reverses an uinteger

Pseudocode
___________
1. Write function reverse_int(num):
2. If num is 0 return num
3. Convert num to an absolute num
4. loop
5. find modulus of num with ten
6. Store in a variable reversed_num
7. update num to the lower limit of num//10
8. return reversed_num
'''

def reverse_int(num):
    abs_num = abs(num)

    if num == 0: return num
    reversed_int = 0
    while abs_num != 0:
        reversed_int = (reversed_int * 10) + (abs_num % 10)
        abs_num //= 10

    if num < 0: return reversed_int * -1
    return reversed_int

result = reverse_int(67845)
print(result)

'''
Time complexity = O(n)
Space complexity = O(1)
'''