from unittest import TestCase, main
from tested.max_pacage import maximizer
from tested.max_pacage.maximizer import maxim_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(maximizer))
    return tests


class MaxTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(maxim_func(a=1, b=2), 2)

    def test_second_zero_in_input(self):
        with self.assertRaises(TypeError) as e:
            maxim_func(a=1, b=0)
        self.assertEqual('введите 2 целых числа, b>0', e.exception.args[0])

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            maxim_func(a=1, b=0)
        self.assertEqual('введите 2 целых числа, b>0', e.exception.args[0])


if __name__ == '__main__':
    main()
