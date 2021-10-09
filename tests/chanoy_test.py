from unittest import TestCase, main
from tested.chanoy_tover_package import chanoy_tower
from tested.chanoy_tover_package.chanoy_tower import move
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(chanoy_tower))
    return tests


class ChanTowerTest(TestCase):
    def test_int_input(self):
        self.assertEqual(move(n=10, start=1, finish=3), (9, 2, 3))

    def test_lit_int_input(self):
        self.assertEqual(move(n=8, start=1, finish=4), (7, 1, 4))

    def test_neg_int_input(self):
        with self.assertRaises(TypeError) as e:
            move(n=-8, start=-1, finish=-4)
        self.assertEqual('введите целые, положительные  числа', e.exception.args[0])

    def test_char_input(self):
        with self.assertRaises(TypeError) as e:
            move(n='8', start='1', finish='4')
        self.assertEqual('введите целые, положительные  числа', e.exception.args[0])


if __name__ == '__main__':
    main()
