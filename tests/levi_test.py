from unittest import TestCase, main
from tested.Levi_dist_package import levi
from tested.Levi_dist_package.levi import distance
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(levi))
    return tests


class LeviTest(TestCase):
    def test_two_strings(self):
        self.assertEqual(distance(a='hi men', b='hi all'), 3)

    def test_digit_in_input(self):
        with self.assertRaises(TypeError) as e:
            distance(a=123, b=456)
        self.assertEqual('Передан неверный тип данных,либо - пустая строка', e.exception.args[0])


if __name__ == '__main__':
    main()
