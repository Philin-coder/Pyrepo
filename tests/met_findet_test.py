from unittest import TestCase, main
from tested.meth_finder_package import met_finder
from tested.meth_finder_package.met_finder import met_finder_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(met_finder))
    return tests


class MetFinderTest(TestCase):
    def test_is_meth_str(self):
        self.assertEqual(met_finder_func(meth='str'),
                         ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
                          '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
                          '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
                          '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
                          '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
                          'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
                          'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
                          'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
                          'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
                          'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
                          'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'])

    def test_is_str_int(self):
        with self.assertRaises(TypeError) as e:
            met_finder_func(meth=123)
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_is_empty(self):
        with self.assertRaises(TypeError) as e:
            met_finder_func(meth='')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
