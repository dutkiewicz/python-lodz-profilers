from timeit import timeit

if __name__ == "__main__":
    print(
        timeit(
            "is_duplicate('x', 'qwertyuiopasdfghjklzxcvbnm'.split())",
            setup="from main import is_duplicate",
        )
    )
