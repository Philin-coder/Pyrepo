from unittest import TestCase, main
from tested.one_more_reverser_package import reverser
from tested.one_more_reverser_package.reverser import reverser_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(reverser))
    return tests


class RevTest(TestCase):
    def test_works(self):
        self.assertEqual(reverser_func(right_list=[1, 2, 3, 4, 5]), 15)

    def test_char_in(self):
        with self.assertRaises(TypeError) as e:
            reverser_func(right_list=['@', 1, 2, 3, 4, 5])
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_set_in(self):
        with self.assertRaises(TypeError) as e:
            reverser_func(right_list={1, 2, 3, 4, 5})
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
