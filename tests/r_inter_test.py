from unittest import TestCase, main
from tested.r_intersection_package import r_inter
from tested.r_intersection_package.r_inter import r_intersection
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(r_inter))
    return tests


class RInterTest(TestCase):
    def test_float_in_input(self):
        self.assertEqual(r_intersection(r=1.0, a=2.0, b=3.4), 'Прямая и окружность не пересекаются')

    def test_spaces_in_input(self):
        with self.assertRaises(TypeError) as e:
            r_intersection(r='', a='', b='')
        self.assertEqual('Введите вещественное число', e.exception.args[0])


if __name__ == '__main__':
    main()
