from unittest import TestCase, main
from tested.count_even_package import count_even
from tested.count_even_package.count_even import cnt_even
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(count_even))
    return tests


class CountEvenTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(cnt_even(n=12), (6, ' ', 5))

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            cnt_even(n='12')
        self.assertEqual('введите число', e.exception.args[0])

    def test_float_in_input(self):
        with self.assertRaises(TypeError) as e:
            cnt_even(n=12.0)
        self.assertEqual('введите число', e.exception.args[0])


if __name__ == '__main__':
    main()
