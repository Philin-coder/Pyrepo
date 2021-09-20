from unittest import TestCase, main
from tested.element_plus_package import elementor
from tested.element_plus_package.elementor import v_sum_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(elementor))
    return tests


class ElementorPlusTest(TestCase):
    def test_n_int(self):
        self.assertEqual(v_sum_func(n=12), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_n_char(self):
        with self.assertRaises(TypeError) as e:
            v_sum_func(n='12'),
        self.assertEqual('Введите  целое положительное число', e.exception.args[0])

    def test_n_neg(self):
        with self.assertRaises(TypeError) as e:
            v_sum_func(n=-12),
        self.assertEqual('Введите  целое положительное число', e.exception.args[0])


if __name__ == '__main__':
    main()
