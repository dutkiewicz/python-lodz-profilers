import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func} :: {end_time - start_time}")
        return value

    return wrapped
