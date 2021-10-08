from unittest import TestCase, main
from tested.uniq_reducr_package import uniq_reducer
from tested.uniq_reducr_package.uniq_reducer import unique_list_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(uniq_reducer))
    return tests


class UniqREducerTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(unique_list_func(work_list=[1, 2, 3, 3, 3, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_char_in_input(self):
        self.assertEqual(unique_list_func(work_list=['a', 'b', 'c', 'c', 'c', 'c', 'd', 'e']),
                         ['a', 'b', 'c', 'd', 'e'])

    def test_empty_ls_in_input(self):
        self.assertEqual(unique_list_func(work_list=[]), [])

    def test_wrong_input_in_input(self):
        with self.assertRaises(TypeError) as e:
            unique_list_func(work_list={})
        self.assertEqual('передан не список', e.exception.args[0])


if __name__ == '__main__':
    main()
