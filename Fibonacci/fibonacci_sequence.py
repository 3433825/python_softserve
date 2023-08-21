def get_element_fibonacci_sequence(n: int) -> int:
    """
    :param n:
    :return: n-element og Fibonacci sequence.
    """

    if not isinstance(n, int):
        raise TypeError(f"argument of fib() must be integers, not {type(n)}")
    return n if n < 2 else get_element_fibonacci_sequence(n - 1) + get_element_fibonacci_sequence(n - 2)
