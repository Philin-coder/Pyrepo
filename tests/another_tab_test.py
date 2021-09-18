from unittest import TestCase, main
from tested.another_tabulatror import tabul
from tested.another_tabulatror.tabul import tab_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(tabul))
    return tests


class TabTest(TestCase):
    def test_tabul_neg(self):
        self.assertEqual(tab_func(x=-1), [3.0])

    def test_tabul_int(self):
        self.assertEqual(tab_func(x=10), [3.0, 7.0, 19.0, 39.0, 67.0, 103.0, 147.0])

    def test_tabul_char(self):
        with self.assertRaises(TypeError) as e:
            tab_func(x='1')
        self.assertEqual('Введите число', e.exception.args[0])


if __name__ == '__main__':
    main()
