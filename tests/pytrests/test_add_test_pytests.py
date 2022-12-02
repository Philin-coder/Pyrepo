import pytest
from tested.add_package import add_example
from tested.add_package.add_example import simple_add_example_func


def test_odd():
    assert simple_add_example_func(x=2, y=3) == 5


def test_even():
    assert simple_add_example_func(x=5, y=5) == 10


def test_float_second(self):
    assert simple_add_example_func(x=5, y=2.5) == 7.5


def test_float_symbol():
    with pytest.raises(TypeError) as error:
        simple_add_example_func(x=5, y='2')
    .assertEqual('введите 2 числа', e.exception.args[0])


if __name__ == '__main__':
    pytest.main()
