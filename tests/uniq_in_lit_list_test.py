from unittest import TestCase, main
from tested.uniq_lit_in_list_package import uniq_lit_in_list
from tested.uniq_lit_in_list_package.uniq_lit_in_list import collect_unique
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(uniq_lit_in_list))
    return tests


class UniqTest(TestCase):
    def test_uniq_in_list_works(self):
        self.assertEqual(collect_unique('проба проба2 проба2'), ['проба', 'проба2'])

    def test_uniq_in_list_works_all_uniq(self):
        self.assertEqual(collect_unique('проба1 проба2 проба3'), ['проба1', 'проба2', 'проба3'])

    def test_uniq_in_list_works_empty_input(self):
        with self.assertRaises(ValueError) as e:
            collect_unique('')
        self.assertEqual('введите строку', e.exception.args[0])

    def test_uniq_in_list_is_str_in(self):
        self.assertTrue(isinstance('проба1 проба2 проба3', str) is True, "Не строка")

    def test_uniq_in_list_is_list_out(self):
        self.assertTrue(isinstance(['проба', 'проба2'], list) is True, "Не лист")


if __name__ == '__main__':
    main()
