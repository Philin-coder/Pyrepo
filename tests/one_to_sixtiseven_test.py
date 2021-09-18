from unittest import TestCase, main
from tested.one_to_sixtiseven_pacage import one_to_sixtiseven
from tested.one_to_sixtiseven_pacage.one_to_sixtiseven import random_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(one_to_sixtiseven))
    return tests


class OneToSixtisevenTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(random_func(p=12, q=2), [2, 14, 26, 38, 50, 62])

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            random_func(p='12', q='2')
        self.assertEqual('введите 2 целых числа', e.exception.args[0])


if __name__ == '__main__':
    main()
