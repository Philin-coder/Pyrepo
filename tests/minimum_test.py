from unittest import TestCase, main
from tested.minimum_demo_package import min_demo
from tested.minimum_demo_package.min_demo import min_in_mas
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(min_demo))
    return tests


class MinTest(TestCase):
    def test_min_test_works(self):
        self.assertEqual(min_in_mas(n=10), 1)

    def test_min_test_three(self):
        self.assertEqual(min_in_mas(n=3), 1)

    def test_min_test_negative(self):
        with self.assertRaises(TypeError) as e:
            min_in_mas(n=-3)
        self.assertEqual('Введите число положительное , не равное 0', e.exception.args[0])

    def test_min_test_zero(self):
        with self.assertRaises(TypeError) as e:
            min_in_mas(n=0)
        self.assertEqual('Введите число положительное , не равное 0', e.exception.args[0])

    def test_min_test_char(self):
        with self.assertRaises(TypeError) as e:
            min_in_mas(n='0')
        self.assertEqual('Введите число положительное , не равное 0', e.exception.args[0])


if __name__ == '__main__':
    main()
