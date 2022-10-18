def fibonacci(n):

    if type(n) != int:
        raise TypeError("n must be a positive int")

    if n < 1:
        raise ValueError("n must be a positive int")

    if n == 1: return 1
    elif n == 2: return 1

    fibonacci_cache = {}
    value = 0

    if n in fibonacci_cache: return fibonacci_cache[n]
    else:
        value = fibonacci(n - 2) + fibonacci(n - 1)

    fibonacci_cache[n] = value

    return value

result = fibonacci(3.3)


print(result)