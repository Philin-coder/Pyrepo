from unittest import TestCase, main
from tested.deleter_test_package import deleter
from tested.deleter_test_package.deleter import before_colons_del
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(deleter))
    return tests


class DeleterTest(TestCase):
    def test_deleteer_works(self):
        self.assertEqual(before_colons_del('проба: первая'), 'проба')

    def test_deleteer_works_no_colons(self):
        self.assertEqual(before_colons_del('проба вторая'), 'проба втора')

    def test_deleteer_works_english(self):
        self.assertEqual(before_colons_del(text_str='colons: двоеточие'), 'colons')

    def test_deleteer_works_english(self):
        self.assertEqual(before_colons_del(text_str=''), '')

    def test_deleteer_ints(self):
        with self.assertRaises(TypeError) as e:
            before_colons_del(text_str=1)
        self.assertEqual('введите строку', e.exception.args[0])

    def test_deleteer_float(self):
        with self.assertRaises(TypeError) as e:
            before_colons_del(text_str=1.0)
        self.assertEqual('введите строку', e.exception.args[0])


if __name__ == '__main__':
    main()
