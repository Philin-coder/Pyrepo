from unittest import TestCase, main
from tested.odd_even_package import odd_even
from tested.odd_even_package.odd_even import count_even_odd_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(odd_even))
    return tests


class OddEvenTest(TestCase):
    def test_even_n(self):
        self.assertEqual(count_even_odd_func(n=12), ('чет[2, 4, 6, 8, 10, 12]', 'нечет[1, 3, 5, 7, 9, 11]'))

    def test_odd_n(self):
        self.assertEqual(count_even_odd_func(n=13), ('чет[2, 4, 6, 8, 10, 12]', 'нечет[1, 3, 5, 7, 9, 11, 13]'))

    def test_zero_n(self):
        self.assertEqual(count_even_odd_func(n=0), ('чет[]', 'нечет[]'))

    def test_char_n(self):
        with self.assertRaises(TypeError) as e:
            count_even_odd_func(n='0')
        self.assertEqual('Введите  целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
