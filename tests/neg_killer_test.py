from unittest import TestCase, main
from tested.neg_killer_package import neg_killer
from tested.neg_killer_package.neg_killer import del_negs
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(neg_killer))
    return tests


class DelNegTest(TestCase):
    def test_del_negs_int_in_input(self):
        self.assertEqual(del_negs(n=12), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_is_del_negs_list(self):
        self.assertIsInstance(del_negs(n=12), list)

    def test_is_ints_in_list(self):
        self.assertTrue((all(isinstance(i, int) for i in del_negs(n=12))) is True, 'В списке не число')

    def test_not_neg(self):
        self.assertTrue((all(i > 0 for i in del_negs(n=12))) is True, 'числа положительные')

    def test_del_negs_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            del_negs(n='12')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
