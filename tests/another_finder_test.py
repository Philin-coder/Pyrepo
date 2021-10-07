from unittest import TestCase, main
from tested.another_finder_package import another_finder
from tested.another_finder_package.another_finder import finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(another_finder))
    return tests


class AnotherFinderTest(TestCase):
    def test_str_in_input_true(self):
        self.assertEqual(finder(text_str='ОН оно но не онв'), True)

    def test_str_in_input_false(self):
        self.assertEqual(finder(text_str='Проба   нет тут ничего не победа'), False)

    def test_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            finder(text_str=1)
        self.assertEqual('Вводите строку', e.exception.args[0])


if __name__ == '__main__':
    main()
