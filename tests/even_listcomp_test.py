from unittest import TestCase, main
from tested.even_listcomp_pacage import even_listcomp
from tested.even_listcomp_pacage.even_listcomp import list_even
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(even_listcomp))
    return tests


class EvenListCompTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(list_even(a=1, b=101),
                         [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48,
                          50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94,
                          96, 98, 100])

    def test_chars_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(list_even(a='1', b='101'))
        self.assertEqual('Долны быть введены 2 целых числа не равных 0', e.exception.args[0])

    def test_lists_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(list_even(a=[1], b=[1, 0, 1]))
        self.assertEqual('Долны быть введены 2 целых числа не равных 0', e.exception.args[0])


if __name__ == '__main__':
    main()
