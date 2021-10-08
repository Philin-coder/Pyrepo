from unittest import TestCase, main
from tested.fib_finder_package import fib_finder
from tested.fib_finder_package.fib_finder import fib_fnd_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(fib_finder))
    return tests


class FibFinderTestCase(TestCase):
    def test_works_int_input(self):
        self.assertEqual(fib_fnd_func(n=12, x=1), 'число 1 содержится в списке')

    def test_works_int_input_no_int(self):
        self.assertEqual(fib_fnd_func(n=12, x=99), 'числа  нет в диапазоне')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            fib_fnd_func(n='12', x='99')
        self.assertEqual('Введите числа', e.exception.args[0])


if __name__ == '__main__':
    main()
