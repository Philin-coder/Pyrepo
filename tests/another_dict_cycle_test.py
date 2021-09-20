from unittest import TestCase, main
from tested.cycle_dict_package import cycle_dict
from tested.cycle_dict_package.cycle_dict import cycle_dict_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cycle_dict))
    return tests


class CycleDictTest(TestCase):
    def test_works(self):
        self.assertEqual(cycle_dict_func(key_list=['раз', 'два', 'Три']), {'раз': 1, 'два': 2, 'Три': 3})

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            cycle_dict_func(key_list={'раз', 'два', 'Три'})
        self.assertEqual('Передане не списсок', e.exception.args[0]),


if __name__ == '__main__':
    main()
