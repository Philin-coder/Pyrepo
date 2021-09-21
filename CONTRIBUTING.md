Данный репозиторий содержит типовые алгоритмические задачи, решенные на языке Python и тесты к ним

_Пример задачи_:
_______________________________________

```python
def dict_count_func(x: float, y: float, key_to_find: str) -> [int, float]:
    """
    Калькулятор работающмй на основе словаря
    :param x:  первый операнд
    :param y: второй операнд
    :param key_to_find:  код операции
    :return: резульат операции
    >>> dict_count_func(x=2, y=5, key_to_find='add')
    7
    >>> dict_count_func(x=2, y=5, key_to_find='sub')
    -3
    >>> dict_count_func(x=2, y=5, key_to_find='mul')
    10
    >>> dict_count_func(x=2, y=5, key_to_find='div')
    0.4

    """
    operations = ('add', 'sub', 'mul', 'div')
    if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) or isinstance(y, int) and any(
            i in key_to_find for i in operations):

        try:
            m_count_dict = {
                'add': lambda a, b: a + b,
                'sub': lambda a, b: a - b,
                'mul': lambda a, b: a * b,
                'div': lambda a, b: a / b

            }
            if key_to_find == 'add':
                return m_count_dict['add'](x, y)
            elif key_to_find == 'sub':
                return m_count_dict['sub'](x, y)
            elif key_to_find == 'mul':
                return m_count_dict['mul'](x, y)
            elif key_to_find == 'div':
                if y == 0:
                    raise ZeroDivisionError('на ноль делить -Зло ')
                else:
                    return m_count_dict['div'](x, y)
        except(TypeError, ValueError):
            raise TypeError(
                'введите 2 числа и код операции(add- сложение, sub- вычитание, mul-умножене, div- деленеи)')
        else:
            raise ValueError('неверно введен код операции')
   ```

Пример текста(на unittest)

```python
from unittest import TestCase, main
from tested.another_calculator_with_dict_package import dict_arifm
from tested.another_calculator_with_dict_package.dict_arifm import counter_again
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dict_arifm))
    return tests


class AnotherCalculatorWithDictTest(TestCase):
    def test_plus(self):
        self.assertEqual(counter_again(a=1, b=2, operation='+'), 3)

    def test_minus(self):
        self.assertEqual(counter_again(a=7, b=1, operation='-'), 6)

    def test_mul(self):
        self.assertEqual(counter_again(a=8, b=2, operation='*'), 16)

    def test_div(self):
        self.assertEqual(counter_again(a=8, b=2, operation='/'), 4.0)

    def test_wrong_sign(self):
        with self.assertRaises(ValueError) as e:
            counter_again(a=8, b=2, operation='&')
        self.assertEqual('Нужных знаков нет', e.exception.args[0])

    def test_chars_in_input(self):
        with self.assertRaises(TypeError) as e:
            counter_again(a=8, b='2', operation='/')
        self.assertEqual('Неверно введен тип операнда', e.exception.args[0])

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError) as e:
            counter_again(a=8, b=0, operation='/')
        self.assertEqual('На ноль делить грешно', e.exception.args[0])


if __name__ == '__main__':
    main()

```