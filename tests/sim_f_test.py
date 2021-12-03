from unittest import TestCase, main
from tested.syn_func_package import sim_f
from tested.syn_func_package.sim_f import count_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sim_f))
    return tests


class SymFunTestCase(TestCase):
    def test_int_in_input(self):
        self.assertEqual(count_func(x=8), 0.22)

    def test_float_in_input(self):
        self.assertEqual(count_func(x=80.0), -1.5)

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            count_func(x='8')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_is_not_None(self):
        self.assertIsNotNone(count_func(x=8))

    def test_if_None(self):
        with self.assertRaises(TypeError) as e:
            count_func(x=None)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_neg(self):
        with self.assertRaises(ValueError) as e:
            count_func(x=-8)
        self.assertEqual('под корнем отрицательное число', e.exception.args[0])


if __name__ == '__main__':
    main()
