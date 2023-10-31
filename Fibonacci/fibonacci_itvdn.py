import timeit


def fib(n: int) -> int:
    """
    :param n:
    :return: n-element of Fibonacci sequence.
    """

    if not isinstance(n, int):
        raise TypeError(f"argument of fib() must be integers, not {type(n)}")
    return n if n < 2 else fib(n - 1) + fib(n - 2)


n = 35
# print(fib(0))
print(f"{n}th element of Fibonacci sequence: {fib(n)}")


execution_time = timeit.timeit(lambda: fib(n), number=1)
print(f"execution_time: {execution_time:.6f} s")


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
