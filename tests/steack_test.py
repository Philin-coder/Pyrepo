from unittest import TestCase, main
from tested.steack_package import steaker
from tested.steack_package.steaker import steak_area_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(steaker))
    return tests


class SteTest(TestCase):
    def test_int_input_no(self):
        self.assertEqual(steak_area_func(x=12, y=11), 'Нет')

    def test_int_input_yes(self):
        self.assertEqual(steak_area_func(x=2, y=2), 'Да')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            steak_area_func(x='2', y='2')
        self.assertEqual('введены не числа', e.exception.args[0])


if __name__ == '__main__':
    main()
