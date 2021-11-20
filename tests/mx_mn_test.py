from unittest import TestCase, main
from tested.max_min_package import max_min
from tested.max_min_package.max_min import max_end_min
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(max_min))
    return tests


class MaxEndMinTest(TestCase):
    def test_max_end_min_right(self):
        self.assertEqual(max_end_min(n=6), (6, 1))

    def test_max_end_min_n_zero(self):
        with self.assertRaises(TypeError) as e:
            max_end_min(n=0),
        self.assertEqual('Передан неверный тип данных, либо - неверное значение диапазона', e.exception.args[0])

    def test_max_end_min_n_neg(self):
        with self.assertRaises(TypeError) as e:
            max_end_min(n=-10),
        self.assertEqual('Передан неверный тип данных, либо - неверное значение диапазона', e.exception.args[0])

    def test_max_end_min_n_char(self):
        with self.assertRaises(TypeError) as e:
            max_end_min(n='6'),
        self.assertEqual('Передан неверный тип данных, либо - неверное значение диапазона', e.exception.args[0])


if __name__ == '__main__':
    main()
