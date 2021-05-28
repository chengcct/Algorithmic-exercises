def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


print(fib(6))
