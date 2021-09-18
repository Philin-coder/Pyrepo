from unittest import TestCase, main
from tested.sum_of_devs_a_package import  sum_of_devs
from tested.sum_of_devs_a_package.sum_of_devs import sum_of_devs_func
import doctest



def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sum_of_devs))
    return tests


class SumOfDEvsTest(TestCase):
    def test_int_input_even(self):
        self.assertEqual(sum_of_devs_func(x=12),78)

    def test_int_input_odd(self):
        self.assertEqual(sum_of_devs_func(x=5), 0)

    def test_int_input_zero(self):
        self.assertEqual(sum_of_devs_func(x=0), 0)

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            sum_of_devs_func(x='0')
        self.assertEqual('Введите целое число',e.exception.args[0])


if __name__ == '__main__':
    main()
