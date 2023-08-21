import  time
import functools
import typing


def duration(func: typing.Callable) -> typing.Callable:
    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        start = time.process_time()
        result = func(*args, **kwargs)
        duration_time = time.process_time() - start
        print(f"{func.__name__} takes {duration_time} seconds")
        return result
    return wrapper_time
