import functools
import typing


def cache(func: typing.Callable) -> typing.Any:
    """Keep a cache of previous function calls."""

    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs)
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


# if __name__ == "__main__":
#     @cache
#     def my_test_func(n):
#         return n ** 2
#
#     for i in range(1, 10):
#         print(my_test_func(i))
