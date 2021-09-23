from unittest import TestCase, main
from tested.fib_package import gen_function_example
from tested.fib_package.gen_function_example import gen_start
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(gen_function_example))
    return tests


class GenFncTest(TestCase):
    def test_gen_works_lot_of(self):
        self.assertEqual(gen_start(a=0, b=1, mx=4000000), 4613732)

    def test_gen_works_even(self):
        self.assertEqual(gen_start(a=1, b=2, mx=10), 10)

    def test_gen_works_odd(self):
        self.assertEqual(gen_start(a=4, b=7, mx=33), 22)

    def test_gen_works_zero(self):
        self.assertEqual(gen_start(a=0, b=0, mx=0), 0)

    def test_gen_works_negs(self):
        with self.assertRaises(TypeError) as e:
            gen_start(a=-10, b=-10, mx=10)
        self.assertEqual(
            'Введите положительные целые числа для шага генератора, максимума, генератора и '
            'начального значения генератора',
            e.exception.args[0])

    def test_gen_chars(self):
        with self.assertRaises(TypeError) as e:
            gen_start(a='10', b=-10, mx=10)
        self.assertEqual(
            'Введите положительные целые числа для шага генератора, максимума, генератора'
            ' и начального значения генератора',
            e.exception.args[0])


if __name__ == '__main__':
    main()
