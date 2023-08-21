def fib(n: int) -> int:
    """
    :param n:
    :return: n-element og Fibonacci sequence.
    """

    if not isinstance(n, int):
        raise TypeError(f"argument of fib() must be integers, not {type(n)}")
    return n if n < 2 else fib(n - 1) + fib(n - 2)


# print(fib(35))


# if __name__ == "__main__":
#     test_cases = [
#         (0, 0),
#         (1, 1),
#         (2, 1),
#         (3, 2),
#         (4, 3)
#     ]
#     for arg, result in test_cases:
#         # print(fib(arg), f"{fib(arg) == result}")
#         assert fib(arg) == result, f"ERROR! fib({arg}) != {result}"