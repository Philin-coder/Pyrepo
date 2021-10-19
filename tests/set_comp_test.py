from unittest import TestCase, main
from tested.set_comp_package import set_mod
from tested.set_comp_package.set_mod import set_analyser_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(set_mod))
    return tests


class SetCompTest(TestCase):
    def test_works_is_same_nums(self):
        self.assertEqual(set_analyser_func(a=1, b=1, c=1), 3)

    def test_works_different_nums(self):
        self.assertEqual(set_analyser_func(a=5, b=8, c=1), 0)

    def test_works_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            set_analyser_func(a='a', b='v', c='c')
        self.assertEqual('передан неправильный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
