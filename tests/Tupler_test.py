from unittest import TestCase, main
from tested.tupler_package import tupler
from tested.tupler_package.tupler import tuple_conv_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(tupler))
    return tests


class TupleTest(TestCase):
    def test_works(self):
        self.assertIsInstance(tuple('hello'), tuple)

    def test_fails(self):
        with self.assertRaises(TypeError) as e:
            tuple_conv_func(text_srt={})
        self.assertEqual('Введите строку', e.exception.args[0])


if __name__ == '__main__':
    main()
