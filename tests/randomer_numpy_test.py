from unittest import TestCase, main
from tested.numpy_random_package import randomer
from tested.numpy_random_package.randomer import numpy_random_func
import doctest
import numpy as np
import random


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(randomer))
    return tests


class MyNPTest(TestCase):
    def test_is_nd_array_list(self):
        self.assertIsInstance(np.array([random.random() for _ in range(4)]), np.ndarray)

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            numpy_random_func(n='3')
        self.assertEqual('введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
