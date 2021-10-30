from unittest import TestCase, main
from tested.min_hours_package import min_h
from tested.min_hours_package.min_h import how_many_hour_and_minutes
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(min_h))
    return tests


class MinHourTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(how_many_hour_and_minutes(n=148), (2, 28))

    def test_ints_in_input_less_twenty_four(self):
        self.assertEqual(how_many_hour_and_minutes(n=14), (0, 14))

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            how_many_hour_and_minutes(n='148')
            self.assertEqual('e', e.exception.args[0])


if __name__ == '__main__':
    main()
