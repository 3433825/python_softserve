from cache import cache


@cache
def fib_simple_cache(n: int) -> int:
    """
    :param n:
    :return: n-element of the Fibonacci sequence.
    """

    if not isinstance(n, int):
        raise TypeError(f"argument of fib() must be integers, not {type(n)}")
    return n if n < 2 else fib_simple_cache(n - 1) + fib_simple_cache(n - 2)


n = 35
print(fib_simple_cache(n))
# execution_time =

