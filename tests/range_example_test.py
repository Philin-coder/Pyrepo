import doctest
from unittest import TestCase, main
from tested.range_examle_package import range_examle
from tested.range_examle_package.range_examle import range_func


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(range_examle))
    return tests


class RangeTest(TestCase):
    def test_bord_ints(self):
        self.assertEqual(range_func(1, 5), [1, 2, 3, 4, 5])

    def test_bord_char(self):
        with self.assertRaises(TypeError) as e:
            range_func('1', '4')
        self.assertEqual('Должны быть введенв 2 целых числа не равных 0', e.exception.args[0])

    def test_bord_spaces(self):
        with self.assertRaises(TypeError) as e:
            range_func(' ', ' ')
        self.assertEqual('Должны быть введенв 2 целых числа не равных 0', e.exception.args[0])


if __name__ == '__main__':
    main()
