import time


def cached_results(func):
    cache: dict = {}

    def wrapper(*args, **kwargs):
        n = args[0]
        if n in cache:
            print(f"Cache hit for {n}: returning cached result.")
            return cache[n]
        else:
            print(f"Calculating result for {n}.")
            result = func(*args, **kwargs)
            cache[n] = result
            print(f"Cache after calculating {n}: {cache}")
            return result

    return wrapper


@cached_results
def fibonacci(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    result = fibonacci(n - 1) + fibonacci(n - 2)
    return result


start = time.perf_counter()
fibonacci(3)
end = time.perf_counter()
print(f"Run time for first uncached call is: {end - start:.5f} sec")
