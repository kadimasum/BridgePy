'''
PROBLEM Write a program that prints the numbers from 1 to 100. If a number
is divisible by 3, print “Fizz” instead of the number, if a number is divisible by
5, print “Buzz” instead of the number, and if a number is divisible by both 3 and 5,
print “FizzBuzz” instead of the number.
'''

def fizz_buzz(N):
    for i in range(1,N+1):
        if i % 3 == 0 and i % 5 == 0: print(f"{i}:FizzBuzz")
        elif i % 3 == 0: print(f"{i}:Fizz")
        elif i % 5 == 0: print(f"{i}:Buzz")
        else: print(f"{i}:Not divisible by either 3 or 5")
fizz_buzz(15)