from unittest import TestCase, main
from tested.coord_quoters_package import coord_full
from tested.coord_quoters_package.coord_full import coord_quoters
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(coord_full))
    return tests


class CoordTest(TestCase):
    def test_coord_ints_in_input_first(self):
        self.assertEqual(coord_quoters(x=10.0, y=10.0), 'первая четврть')

    def test_coord_ints_in_input_second(self):
        self.assertEqual(coord_quoters(x=-10.0, y=10.0), 'вторая четврть')

    def test_coord_ints_in_input_third(self):
        self.assertEqual(coord_quoters(x=-10.0, y=0.0), 'третья четврть')

    def test_coord_ints_in_input_fourth(self):
        self.assertEqual(coord_quoters(x=11.0, y=-5.0), 'четвертая четврть')

    def test_coord_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            coord_quoters(x='11.0', y=-5.0)
        self.assertEqual('Введите 2 вещественных числа', e.exception.args[0])


if __name__ == '__main__':
    main()
