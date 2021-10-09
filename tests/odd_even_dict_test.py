from unittest import TestCase, main
from tested.odd_even_dict_package import odd_even_dict
from tested.odd_even_dict_package.odd_even_dict import odd_even_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(odd_even_dict))
    return tests


class OddEvenDictTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(odd_even_func(a=1, b=8),
                         {1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True})

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            odd_even_func(a='a', b='b')
        self.assertEqual('Введите целые положительные числа', e.exception.args[0])

    def test_neg_in_input(self):
        with self.assertRaises(TypeError) as e:
            odd_even_func(a=-1, b=8)
        self.assertEqual('Введите целые положительные числа', e.exception.args[0])


if __name__ == '__main__':
    main()
