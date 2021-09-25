from unittest import TestCase, main
from tested.reduce_test_package import reducer
from tested.reduce_test_package.reducer import multer_reduce_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(reducer))
    return tests


class RedTest(TestCase):
    def test_reducer_int_in_input(self):
        self.assertEqual(multer_reduce_func(n=10), 3628800)

    def test_reducer_zero_in_in_input(self):
        self.assertEqual(multer_reduce_func(n=0), 1)

    def test_reducer_one_in_in_input(self):
        self.assertEqual(multer_reduce_func(n=1), 1)

    def test_reducer_char_in_in_input(self):
        with self.assertRaises(TypeError) as e:
            multer_reduce_func(n='10')
        self.assertEqual('Введите число', e.exception.args[0])


if __name__ == '__main__':
    main()
