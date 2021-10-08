from unittest import TestCase, main
from tested.dict_illustrate_pacage import dictum
from tested.dict_illustrate_pacage.dictum import dict_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dictum))
    return tests


class ListZipTest(TestCase):
    def test_dict_works(self):
        self.assertEqual(dict_func(), 'Лена живет в  городе Обнинск')


if __name__ == '__main__':
    main()
