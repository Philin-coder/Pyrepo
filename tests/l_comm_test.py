from unittest import TestCase, main
from tested.big_l_comp_example_package import l_comp
from tested.big_l_comp_example_package.l_comp import list_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(l_comp))
    return tests


class L_compTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(list_func(n=1024), 52020)

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            list_func('f')
        self.assertEqual('Введено не число', e.exception.args[0])

    def test_list_in_input(self):
        with self.assertRaises(TypeError) as e:
            list_func(n=[1, 2, 3])
        self.assertEqual('Введено не число', e.exception.args[0])

    def test_empty_str_in_input(self):
        with self.assertRaises(TypeError) as e:
            list_func(n='')
        self.assertEqual('Введено не число', e.exception.args[0])


if __name__ == '__main__':
    main()
