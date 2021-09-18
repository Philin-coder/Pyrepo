from unittest import TestCase, main
from tested.full_house_package import full_house
from  tested.full_house_package.full_house import full_house_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(full_house))
    return tests


class FullHouseTest(TestCase):
    def test_full_house_right_ints(self):
        self.assertEqual(full_house_func(n=4, k=1), 1)

    def test_full_house_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            full_house_func(n='4', k='1')
        self.assertEqual('Введите целые числа', e.exception.args[0])


if __name__ == '__main__':
    main()
