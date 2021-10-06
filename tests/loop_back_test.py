from unittest import TestCase, main
from tested.loop_back_package import loop_back
from tested.loop_back_package.loop_back import loop_back_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(loop_back))
    return tests


class LoopBackTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(loop_back_func(n=12), [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            loop_back_func(n='12'),
        self.assertEqual('Введите целое положительное число', e.exception.args[0])


if __name__ == '__main__':
    main()
