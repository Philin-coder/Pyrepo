from unittest import TestCase, main
from tested.shufler_package import shufler
from tested.shufler_package.shufler import randomer
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(shufler))
    return tests


class MyShuffleTest(TestCase):
    def test_is_list(self):
        self.assertTrue(randomer(n=9), list)

    def test_is_int_in_list(self):
        self.assertTrue((all(isinstance(i, int) for i in randomer(n=9))) is True)

    def test_is_not_None(self):
        self.assertIsNotNone(randomer(n=9))

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            randomer(n='9')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
