from unittest import TestCase, main
from tested.uniq_simple_range_package import sim_range
from tested.uniq_simple_range_package.sim_range import sim_list_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sim_range))
    return tests


class SimRangeTest(TestCase):
    def test_int_input(self):
        self.assertEqual(sim_list_func(n=300), False)

    def test_int_input_flag_true(self):
        self.assertEqual(sim_list_func(n=3), True)

    def test_int_input_flag_neg(self):
        self.assertEqual(sim_list_func(n=-3), False)

    def test_int_wrong(self):
        with self.assertRaises(TypeError) as e:
            sim_list_func(n='3')
        self.assertEqual('введено не число', e.exception.args[0])


if __name__ == '__main__':
    main()
