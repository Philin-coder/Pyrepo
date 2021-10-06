from unittest import TestCase, main
from tested.templ_package import templ_finder
from tested.templ_package.templ_finder import file_finder_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(templ_finder))
    return tests


class TempTest(TestCase):
    def test_works(self):
        self.assertEqual(file_finder_func(text_str='mp3'), [])

    def test_wrong(self):
        with self.assertRaises(TypeError) as e:
            file_finder_func(text_str={})
        self.assertEqual('Введена не строка', e.exception.args[0])


if __name__ == '__main__':
    main()
