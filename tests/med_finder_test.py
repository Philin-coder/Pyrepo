from unittest import TestCase, main
from tested.med_finder_package import med_finder
from tested.med_finder_package.med_finder import median_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(med_finder))
    return tests


class MedFinderTest(TestCase):
    def test_medfiler_works(self):
        self.assertEqual(median_finder(n=11),6.5)

    def test_medfiler_works_ints_in_input(self):
        self.assertEqual(median_finder(n=10), 5)

    def test_medfiler_works_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            median_finder(n='10')
        self.assertEqual('Введите положительное, целое число не равное 0',e.exception.args[0])

    def test_medfiler_works_negative_in_input(self):
        with self.assertRaises(TypeError) as e:
            median_finder(n=-10)
        self.assertEqual('Введите положительное, целое число не равное 0', e.exception.args[0])

    def test_medfiler_works_zero_in_input(self):
        with self.assertRaises(TypeError) as e:
            median_finder(n=-0)
        self.assertEqual('Введите положительное, целое число не равное 0', e.exception.args[0])


if __name__ == '__main__':
    main()
