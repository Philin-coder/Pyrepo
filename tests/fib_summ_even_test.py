from unittest import TestCase, main
from tested.fib_summ_even_again_package import fib_sum_even
from tested.fib_summ_even_again_package.fib_sum_even import fib_summ_even_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(fib_sum_even))
    return tests


class FibSumTest(TestCase):
    def test_fib_works(self):
        self.assertEqual(fib_summ_even_func(previous=0, next_=1), 4613732)

    def test_works_odd(self):
        self.assertEqual(fib_summ_even_func(previous=1, next_=5), 16019504)

    def test_works_even(self):
        self.assertEqual(fib_summ_even_func(previous=8, next_=10), 4749426)

    def test_zeros_both(self):
        with self.assertRaises(TypeError) as e:
            fib_summ_even_func(previous=0, next_=0)
        self.assertEqual('Введите целые положительные числа больше 0(шаг) для параметра начала исчисления и шага',
                         e.exception.args[0])

    def test_negs(self):
        with self.assertRaises(TypeError) as e:
            fib_summ_even_func(previous=0, next_=0)
        self.assertEqual('Введите целые положительные числа больше 0(шаг) для параметра начала исчисления и шага',
                         e.exception.args[0])

    def test_symbols(self):
        with self.assertRaises(TypeError) as e:
            fib_summ_even_func(previous='0', next_=10)
        self.assertEqual('Введите целые положительные числа больше 0(шаг) для параметра начала исчисления и шага',
                         e.exception.args[0])


if __name__ == '__main__':
    main()
