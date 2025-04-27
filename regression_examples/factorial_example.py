def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


x = 7
print(factorial(x))
