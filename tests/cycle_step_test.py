from unittest import TestCase, main
from tested.cycle_with_step_package import cycle_steper
from tested.cycle_with_step_package.cycle_steper import cycle_step
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cycle_steper))
    return tests


class CycleStepTest(TestCase):
    def test_cycle_step_works_ints_in_inputs(self):
        self.assertEqual(cycle_step(a=1, b=8, step=2), [1, 3, 5, 7])

    def test_cycle_step_works_ints_in_inputs(self):
        self.assertEqual(cycle_step(a=1, b=8, step=1), [1, 2, 3, 4, 5, 6, 7])

    def test_cycle_step_works_ints_neg_in_inputs(self):
        self.assertEqual(cycle_step(a=-10, b=10, step=1),
                         [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_cycle_step_works_zero_in_inputs(self):
        with self.assertRaises(TypeError) as e:
            cycle_step(a=-10, b=10, step=0)
        self.assertEqual('Введите 3 целых положительных числа(начало диапазрна, конец диапазона и шаг )',
                         e.exception.args[0])

    def test_cycle_step_works_chars_in_inputs(self):
        with self.assertRaises(TypeError) as e:
            cycle_step(a=-10, b=10, step='')
        self.assertEqual('Введите 3 целых положительных числа(начало диапазрна, конец диапазона и шаг )',
                         e.exception.args[0])


if __name__ == '__main__':
    main()
