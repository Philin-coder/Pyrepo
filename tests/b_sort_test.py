from unittest import TestCase, main
from tested.classic_soting_package import b_sorting
from tested.classic_soting_package.b_sorting import bubble_sort
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(b_sorting))
    return tests


class BTest(TestCase):
    def test_working(self):
        self.assertEqual(bubble_sort(n=10), [22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 19, 16, 13, 10])

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            bubble_sort(n='10')
        self.assertEqual('Ведите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
