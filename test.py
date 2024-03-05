import pytest
import main
from contextlib import nullcontext as does_not_raise


def test_sum():
    x = 1
    y = 2
    assert main.summary(x, y) == 3


def test_value_error():
    x = 1.0
    y = 2.0
    with pytest.raises(ValueError):
        assert main.multiply(x, y)
    with does_not_raise():
        assert main.multiply(1, 2)


@pytest.mark.parametrize(
    'x, y, result',
    [
        (1, 2, 3),
        (2, 3, 5),
        (4, 6, 10)
    ]
)
def test_parametrize(x, y, result):
    assert main.summary(x, y) == result


@pytest.mark.parametrize(
    'x, y, result, exp',
    [
        (1, 2.0, 2, pytest.raises(ValueError)),
        (2, 3, 6, does_not_raise()),
        (4, 6, 24, does_not_raise())
    ]
)
def test_parametrize_with_errors(x, y, result, exp):
    with exp:
        assert main.multiply(x, y) == result


def single_value(x, y, res_sum, res_multi):
    assert main.summary(x, y) == res_sum
    assert main.multiply(x, y) == res_multi


def test_multi_sum():
    x = [1, 2, 3, 4]
    y = [2, 4, 5, 9]
    res_sum = [3, 6, 8, 13]
    res_multi = [2, 8, 15, 36]
    for i in range(0, 4):
        single_value(x[i], y[i], res_sum[i], res_multi[i])
