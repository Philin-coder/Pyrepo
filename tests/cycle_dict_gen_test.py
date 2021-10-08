from unittest import TestCase, main
from tested.dict_cycle_gen_package import divt_gen
from tested.dict_cycle_gen_package.divt_gen import dict_gen_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(divt_gen))
    return tests


class DictTestTest(TestCase):
    def test_works(self):
        self.assertEqual(dict_gen_func(), {'раз': 1, 'два': 2, 'три': 3})

    def test_is_dict(self):
        self.assertIsInstance({k: i + 1 for i, k in enumerate(['раз', 'два', 'три'])}, dict, 'передан не словарь')

    def test_is_dict_true(self):
        self.assertTrue((isinstance({k: i + 1 for i, k in enumerate(['раз', 'два', 'три'])}, dict)) is True,
                        'передан не словарь')

    def test_is_dict_false(self):
        self.assertFalse(isinstance({k: i + 1 for i, k in enumerate(['раз', 'два', 'три'])}, set) is True,
                         'передан не словарь')


if __name__ == '__main__':
    main()
