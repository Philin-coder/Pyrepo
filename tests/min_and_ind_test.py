from unittest import TestCase, main
from tested.min_and_index_package import min_and_index
from tested.min_and_index_package.min_and_index import min_and_index_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(min_and_index))
    return tests


class MinAndIndTest(TestCase):
    def test_min_and_ind_list_in_input(self):
        self.assertEqual(min_and_index_func(ints=[4, 7, -3, 1, -7, 11, 6]), 'Минимальный 5-й элемент массива = -7')

    def test_min_and_ind_tuple_in_input(self):
        with self.assertRaises(TypeError) as e:
            min_and_index_func(ints=(4, 7, -3, 1, -7, 11, 6))
        self.assertEqual('Получен не список а, tuple', e.exception.args[0])

    def test_min_and_ind_set_in_input(self):
        with self.assertRaises(TypeError) as e:
            min_and_index_func(ints={4, 7, -3, 1, -7, 11, 6})
        self.assertEqual('Получен не список а, set', e.exception.args[0])

    def test_min_and_ind_str_in_input(self):
        with self.assertRaises(TypeError) as e:
            min_and_index_func(ints='4, 7, -3, 1, -7, 11, 6')
        self.assertEqual('Получен не список а, str', e.exception.args[0])


if __name__ == '__main__':
    main()
