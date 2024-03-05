def summary(x: int, y: int) -> int:
    return x + y


def divide(x: int, y: int) -> float:
    return x / y


def multiply(x: int, y: int) -> int:
    if type(x) != int or type(y) != int:
        raise ValueError
    return x * y
