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


CALL_COUNTER = {}


def call_counter(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if func.__name__ not in CALL_COUNTER.keys():
            CALL_COUNTER[func.__name__] = 1
        else:
            CALL_COUNTER[func.__name__] += 1
        value = func(*args, **kwargs)
        return value

    return wrapped
