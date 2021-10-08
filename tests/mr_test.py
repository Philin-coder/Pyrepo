from unittest import TestCase, main
from tested.mr_package import mr
from tested.mr_package.mr import range_filter
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mr))
    return tests


class RandomizerTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(range_filter(n=12), [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_chars_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(range_filter('12'))
        self.assertEqual('должно быть введено целое, положительное число не равное 0 ', e.exception.args[0])


if __name__ == '__main__':
    main()
