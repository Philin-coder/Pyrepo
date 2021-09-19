from unittest import TestCase, main
from tested.Nod_euklidas_packahe import Nod
from tested.Nod_euklidas_packahe.Nod import gcd_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(Nod))
    return tests


class NodTest(TestCase):
    def test_ints_in_input_a_more(self):
        self.assertEqual(gcd_func(a=12, b=2), 2)

    def test_ints_in_input_b_more(self):
        self.assertEqual(gcd_func(a=2, b=5), 1)

    def test_zero_in_input(self):
        with self.assertRaises(TypeError) as e:
            gcd_func(a=0, b=0)
        self.assertEqual('введите целые числа больше 0', e.exception.args[0])

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            gcd_func(a='4', b=8)
        self.assertEqual('введите целые числа больше 0', e.exception.args[0])


if __name__ == '__main__':
    main()
