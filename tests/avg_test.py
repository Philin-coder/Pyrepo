from unittest import TestCase, main
from tested.avg_list_finder_package import avg_finder
from tested.avg_list_finder_package.avg_finder import avg_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(avg_finder))
    return tests


class AvgTest(TestCase):
    def test_avg_works(self):
        self.assertEqual(avg_func(n=10), 5.5)

    def test_avg_works_odd(self):
        self.assertEqual(avg_func(n=11), 6.0)

    def test_avg_works_one(self):
        self.assertEqual(avg_func(n=1), 1.0)

    def test_avg_negative(self):
        with self.assertRaises(TypeError) as e:
            avg_func(n=-1)
        self.assertEqual('Введите целое положительное число больше 0', e.exception.args[0])

    def test_avg_zero(self):
        with self.assertRaises(TypeError) as e:
            avg_func(n=0)
        self.assertEqual('Введите целое положительное число больше 0', e.exception.args[0])


if __name__ == '__main__':
    main()
