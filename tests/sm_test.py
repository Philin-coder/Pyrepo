from unittest import TestCase, main
from tested.simpler import sm
from tested.simpler.sm import is_prime
from tested.simpler.sm import list_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sm))
    return tests


class SimplerTest(TestCase):
    def test_is_prime_int_input_true(self):
        self.assertEqual(is_prime(i=1), True)

    def test_is_prime_int_input_false(self):
        self.assertEqual(is_prime(i=21), False)

    def test_is_prime_char_input(self):
        with self.assertRaises(TypeError) as e:
            is_prime(i='21')
        self.assertEqual('Введено не число', e.exception.args[0])

    def test_list_gen_int_input_even(self):
        self.assertEqual(list_gen(n=100),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97])

    def test_list_gen_int_input_odd(self):
        self.assertEqual(list_gen(n=7), [2, 3, 5])

    def test_list_gen_int_input_empty_list(self):
        self.assertEqual(list_gen(n=1), [])

    def test_list_gen_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            list_gen(n='10')
        self.assertEqual('Введите положительное  число не равное 0', e.exception.args[0])

    def test_list_gen_zero_input(self):
        with self.assertRaises(TypeError) as e:
            list_gen(n=0)
        self.assertEqual('Введите положительное  число не равное 0', e.exception.args[0])

    def test_list_gen_neg_input(self):
        with self.assertRaises(TypeError) as e:
            list_gen(n=-10)
        self.assertEqual('Введите положительное  число не равное 0', e.exception.args[0])


if __name__ == '__main__':
    main()
