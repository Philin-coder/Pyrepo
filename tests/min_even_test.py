from unittest import TestCase, main
from tested.min_even_package import min_even
from tested.min_even_package.min_even import min_evan_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(min_even))
    return tests


class MinEvenTest(TestCase):
    def test_min_even_works(self):
        self.assertEqual(min_evan_func(start_step=2, n=8), 2)

    def test_min_even_works_odd(self):
        self.assertEqual(min_evan_func(start_step=1, n=10), 'минимум не четный,он равен 1')

    def test_min_even_works_zero(self):
        self.assertEqual(min_evan_func(start_step=0, n=0), 0)

    def test_min_even_works_empty(self):
        with self.assertRaises(TypeError) as e:
            min_evan_func(start_step='', n='')
        self.assertEqual('введите 2 целых числа(начало и конец диапазона)', e.exception.args[0])

    def test_min_even_works_char(self):
        with self.assertRaises(TypeError) as e:
            min_evan_func(start_step='1', n=10)
        self.assertEqual('введите 2 целых числа(начало и конец диапазона)', e.exception.args[0])


if __name__ == '__main__':
    main()
