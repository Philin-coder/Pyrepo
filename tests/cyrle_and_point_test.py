from unittest import TestCase, main
from tested.cyrcle_and_point_package import cyrcle_and_point
from tested.cyrcle_and_point_package.cyrcle_and_point import func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cyrcle_and_point))
    return tests


class CyrcleAndPOintTest(TestCase):
    def test_it_works_yes(self):
        self.assertEqual(func(x=1.0, y=1.0, xc=1.0, yc=1.0, r=1.0), 'yes')

    def test_it_works_no(self):
        self.assertEqual(func(x=220.0, y=20.0, xc=2.0, yc=2.0, r=0.0), 'No')

    def test_it_works_chars_in_input(self):
        with self.assertRaises(TypeError) as e:
            func(x='220.0', y='20.0', xc='2.0', yc='2.0', r='0.0')
        self.assertEqual('Введите вещественные числа', e.exception.args[0])


if __name__ == '__main__':
    main()
