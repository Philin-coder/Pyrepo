from unittest import TestCase, main
from tested.pointandquoters import quoters
from tested.pointandquoters.quoters import coordinate_quoters
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(quoters))
    return tests


class QuotersTest(TestCase):
    def test_int_coords(self):
        self.assertEqual(coordinate_quoters(3, 4), True)

    def test_flat_in_coords(self):
        self.assertEqual(coordinate_quoters(-3.5, 8), True)

    def test_char_in_coords(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(coordinate_quoters('1', '4'))
        self.assertEqual('Должны быть введены числа, целые, либо вещественные', e.exception.args[0])

    def test_list_in_coords(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(coordinate_quoters([1, 2, 3, 4], [1, 2, 3]))
        self.assertEqual('Должны быть введены числа, целые, либо вещественные', e.exception.args[0])

    def test_empty_coords(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(coordinate_quoters('', ''))
        self.assertEqual('Должны быть введены числа, целые, либо вещественные', e.exception.args[0])


if __name__ == '__main__':
    main()
