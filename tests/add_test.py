from unittest import TestCase, main
from tested.add_package import add_example
from tested.add_package.add_example import simple_add_example_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(add_example))
    return tests


class AddTest(TestCase):
    def test_odd(self):
        self.assertEqual(simple_add_example_func(x=2, y=3), 5)

    def test_even(self):
        self.assertEqual(simple_add_example_func(x=5, y=5), 10)

    def test_float_second(self):
        self.assertEqual(simple_add_example_func(x=5, y=2.5), 7.5)

    def test_float_symbol(self):
        with self.assertRaises(TypeError) as e:
            simple_add_example_func(x=5, y='2')
        self.assertEqual('введите 2 числа', e.exception.args[0])


if __name__ == '__main__':
    main()
