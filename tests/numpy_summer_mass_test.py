from unittest import TestCase, main
from tested.numpy_mass_summer_package import summer
from tested.numpy_mass_summer_package.summer import mas_summer
import doctest
import numpy as np


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(summer))
    return tests


class NumpySummerTestCase(TestCase):
    def test_is_matrix(self):
        self.assertIsInstance(mas_summer(a=np.ndarray([1, 2, 3]), b=np.ndarray([1, 2, 3])), np.ndarray)


if __name__ == '__main__':
    main()
