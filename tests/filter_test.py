from unittest import TestCase, main
from tested.lambda_filter import lambda_filter_mod
from tested.lambda_filter.lambda_filter_mod import list_filter_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lambda_filter_mod))
    return tests


class FilTest(TestCase):
    def test_works_is_in(self):
        self.assertEqual(list_filter_func('просо'), ['просо', 'просо', 'просо', 'просо', 'просо'])

    def test_works_is_in_two(self):
        self.assertEqual(list_filter_func('мак'), ['мак', 'мак', 'мак', 'мак', 'мак'])

    def test_works_is_not_in(self):
        self.assertEqual(list_filter_func('пшено'), [])

    def test_masked_digs(self):
        with self.assertRaises(TypeError) as e:
            list_filter_func('121')
        self.assertEqual('Введите строку', e.exception.args[0])

    def test_pure_digs(self):
        with self.assertRaises(TypeError) as e:
            list_filter_func(121)
        self.assertEqual('Введите строку', e.exception.args[0])


if __name__ == '__main__':
    main()
