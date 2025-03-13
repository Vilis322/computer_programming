import pytest


def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for (arg, expected) in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Argument {arg} must be of type {type(expected)}, got {type(arg)} instead.")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int, int)
def add(x, y):
    return x + y


@type_check(str, int)
def repeat_word(word, times):
    return word * times


def test_add_valid():
    assert add(2, 3) == 5


def test_repeat_word_valid():
    assert repeat_word("Hello", 3) == "HelloHelloHello"


def test_add_invalid():
    with pytest.raises(TypeError, match=r"Argument .* must be of type .*"):
        add(2, "3")


def test_repeat_word_invalid():
    with pytest.raises(TypeError, match=r"Argument .* must be of type .*"):
        repeat_word("Hello", "3")


if __name__ == "__main__":
    pytest.main()
