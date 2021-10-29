from unittest import TestCase, main
from tested. happy_nuns_package import h_nums
from tested.happy_nuns_package.h_nums import get_lucky
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(h_nums))
    return tests


class HappyNumsTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(get_lucky(n=7), (128, 4))

    def test_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            get_lucky(n='7')
        self.assertEqual('Введите число', e.exception.args[0])


if __name__ == '__main__':
    main()
