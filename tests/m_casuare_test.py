from unittest import TestCase, main
from tested.another_clouse_package import m_closuare
from tested.another_clouse_package.m_closuare import multiplier
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(m_closuare))
    return tests


class MyClosTest(TestCase):
    def setUp(self):
        self.ml = multiplier(n=2)
        multiplier(n=5)

    def test_works_ints_in_input(self):
        self.ml = multiplier(n=2)
        self.assertEqual(self.ml(5), 10)

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            self.ml = multiplier(n='5')
        self.assertEqual('Введите числа', e.exception.args[0])


if __name__ == '__main__':
    main()
