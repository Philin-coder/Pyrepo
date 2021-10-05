from unittest import TestCase, main
from tested.half_list_package import half_lister
from tested.half_list_package.half_lister import half_list_gen_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(half_lister))
    return tests


class HalfTest(TestCase):
    def test_int_input(self):
        self.assertEqual(half_list_gen_func(n=10), ([6, 7, 8, 9, 10], [1, 2, 3, 4, 5]))

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            half_list_gen_func(n='10')
        self.assertEqual('can only concatenate str (not "int") to str', e.exception.args[0])


if __name__ == '__main__':
    main()
