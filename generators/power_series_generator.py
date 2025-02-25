from typing import Iterator


def power_series(x: int | float) -> Iterator[int | float]:
    """Generates an infinite sequence of powers of the given base number x.

    Args:
        x (int or float): The base number for the power series.

    Yields:
        int or float: The next power of the number x (x^n), where n starts at 0 and increments with each iteration.

    Raises:
        TypeError: If x is not of type 'int' or 'float'.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a numeric value.")

    power = 0
    while True:
        yield x ** power
        power += 1


if __name__ == "__main__":
    gen = power_series(2)
    print([next(gen) for _ in range(5)])  # Output: [1, 2, 4, 8, 16]

    # test block
    try:
        gen = power_series(2, 3)
        print(next(gen))
    except TypeError as e:
        print(str(e))

    try:
        gen = power_series("asf")
        print(next(gen))
    except TypeError as e:
        print(str(e))
