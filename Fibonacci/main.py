from fibonacci_itvdn import fib
from fibonacci_simple_cache import fib_simple_cache
from duration import duration


@duration
def main_simple(n: int) -> int:
    return fib(n)


@duration
def main_simple_cache(n: int) -> int:
    return fib_simple_cache(n)


if __name__ == "__main__":
    n = 3
    print(main_simple(n))
    print()
    print(main_simple_cache(n))
