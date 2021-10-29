from unittest import TestCase, main
from tested.lin_package import linar
from tested.lin_package.linar import lin_list
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(linar))
    return tests


class MyLinTest(TestCase):
    def test_works(self):
        self.assertEqual(lin_list(vals=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_works_with_char(self):
        self.assertEqual(lin_list(vals=[[1, 2, 3], [4, 5, 6], [7, 8, 9, 'f']]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 'f'])

    def test_works_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            lin_list(vals=([1, 2, 3], [4, 5, 6], [7, 8, 9, 'f']))
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
