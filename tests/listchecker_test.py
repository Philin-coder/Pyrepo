import doctest
from unittest import TestCase, main
from tested.any_list_input_package.list_checker import inp_list
from tested.any_list_input_package import list_checker


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(list_checker))
    return tests


class ListCheckerTest(TestCase):
    def test_is_list(self):
        self.assertEqual(inp_list(any_data=[1, 2, 3]), 'list')

    def test_type_str(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(inp_list(any_data='123'))
        self.assertEqual('Ввели  не лист', e.exception.args[0])


if __name__ == '__main__':
    main()
