from unittest import TestCase, main
from tested.list_input_package import inputer
from tested.list_input_package.inputer import inp_list
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(inputer))
    return tests


class InputTest(TestCase):
    def test_ints_in(self):
        self.assertEqual(inp_list([1, 2, 3]), [1, 2, 3])

    def test_is_int_in_list(self):
        with self.assertRaises(TypeError) as e:
            inp_list(['right', 'False', 'gbn'])
        self.assertEqual('В списке должны быть целые числа, он не должен быть пуст', e.exception.args[0])


if __name__ == '__main__':
    main()
