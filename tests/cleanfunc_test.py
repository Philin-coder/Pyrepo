from unittest import TestCase, main
import doctest
from tested.cleanfunc_package import cleanf
from tested.cleanfunc_package.cleanf import func


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cleanf))
    return tests


class CleanFuncTest(TestCase):
    def test_is_all_ints(self):
        self.assertEqual(func(12, 12), 24)

    def test_is_a_string(self):
        with self.assertRaises(ValueError) as e:
            func('12', 12)
        self.assertEqual('проверьте входные данные', e.exception.args[0])

    def test_is_b_string(self):
        with self.assertRaises(ValueError) as e:
            func(12, '12')
            self.assertEqual('проверьте входные данные', e.exception.args[0])

if __name__ == '__main__':
    main()
