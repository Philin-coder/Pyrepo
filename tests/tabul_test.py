from unittest import TestCase, main
from tested.tabul_package import tabul
from  tested.tabul_package.tabul import tab_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(tabul))
    return tests


class TabulTest(TestCase):
    def test_tabul_works_float(self):
        self.assertEqual(tab_func(dx=0.25),
                         [0.0, 0.00390625, 0.0625, 0.31640625, 1.0, 2.44140625, 5.0625, 9.37890625, 16.0, 25.62890625])

    def test_tabul_works_ints(self):
        self.assertEqual(tab_func(dx=25), [0, 390625])

    def test_tabul_works_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            tab_func(dx='25')
        self.assertEqual('Введено не   число', e.exception.args[0])

if __name__ == '__main__':
    main()
