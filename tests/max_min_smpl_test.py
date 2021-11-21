from unittest import TestCase, main
from tested.max_min_simple_package import mx_mn
from tested.max_min_simple_package.mx_mn import min_max
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mx_mn))
    return tests


class MxMLTestCase(TestCase):
    def test_max_end_min_right(self):
        self.assertEqual(min_max(arr=[1, 2, 3, 4, 5, 6]), (1, 6))

    def test_max_end_min_is_not_list(self):
        with self.assertRaises(TypeError) as e:
            min_max(arr={1, 2, 3, 4, 5, 6})
        self.assertEqual('передан неверный тип данных, либо пустой список', e.exception.args[0])

    def test_max_end_min_is_empty(self):
        with self.assertRaises(TypeError) as e:
            min_max(arr=[])
        self.assertEqual('передан неверный тип данных, либо пустой список', e.exception.args[0])


if __name__ == '__main__':
    main()
