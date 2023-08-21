from functools import lru_cache


@lru_cache(maxsize=100)
def fib_lru_cache(n: int) -> int:
    """
    :param n:
    :return: n-element of the Fibonacci sequence.
    """

    if not isinstance(n, int):
        raise TypeError(f"argument of fib() must be integers, not {type(n)}")
    return n if n < 2 else fib_lru_cache(n - 1) + fib_lru_cache(n - 2)