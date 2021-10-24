from unittest import TestCase, main
from tested.random_letter_paclage import random_letter
from tested.random_letter_paclage.random_letter import alpha_random_nums
import doctest
import random


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(random_letter))
    return tests


class MyRandLetTest(TestCase):
    def setUp(self):
        self.lt = alpha_random_nums(start_p=97, end_p=123, n=14)

    def test_is_random_int(self):
        self.assertTrue((96 <= random.randint(96, 123) <= 123) is True, 'НЕ попадает  в диапазон')

    def test_wrong_input(self):
        with self.assertRaises(ValueError) as e:
            self.lt = alpha_random_nums(start_p=90, end_p=121, n=114)

        self.assertEqual('проверьте диапазон', e.exception.args[0])

    def test_wrong_input_zeros(self):
        with self.assertRaises(ValueError) as e:
            self.lt = alpha_random_nums(start_p=0, end_p=0, n=0)
        self.assertEqual('проверьте диапазон', e.exception.args[0])

    def test_wrong_input_chars(self):
        with self.assertRaises(TypeError) as e:
            self.lt = alpha_random_nums(start_p='90', end_p='121', n='114')
        self.assertEqual('Введите целые числа', e.exception.args[0])


if __name__ == '__main__':
    main()
