from unittest import TestCase, main
from tested.tabulation_with_step_package import tabul
from tested.tabulation_with_step_package.tabul import tab_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(tabul))
    return tests


class TabulStepTest(TestCase):
    def test_normal_input_dx_float(self):
        self.assertEqual(tab_func(dx=0.1, x=2),
                         [3.0, 3.01, 3.04, 3.09, 3.16, 3.25, 3.36, 3.4899999999999998, 3.6399999999999997,
                          3.8099999999999996, 4.0, 4.21, 4.4399999999999995, 4.69, 4.960000000000001, 5.250000000000001,
                          5.5600000000000005, 5.8900000000000015, 6.240000000000002, 6.610000000000002,
                          7.000000000000002])

    def test_normal_input_dx_int(self):
        self.assertEqual(tab_func(dx=10, x=1), [3, 103])

    def test_normal_input_dx_hundred(self):
        self.assertEqual(tab_func(dx=100, x=12), [3, 10003])

    def test_normal_input_dx_char(self):
        with self.assertRaises(TypeError) as e:
            tab_func(dx='100', x=-12)
        self.assertEqual('Введите число',e.exception.args[0])

    def test_normal_input_x_char(self):
        with self.assertRaises(TypeError) as e:
            tab_func(dx=100, x='12')
        self.assertEqual('Введите число', e.exception.args[0])


if __name__ == '__main__':
    main()
