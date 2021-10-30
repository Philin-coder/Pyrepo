from unittest import TestCase, main
from tested.numpy_mass_summer_package import summer
from tested.numpy_mass_summer_package.summer import mas_summer
import doctest
import numpy as np


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(summer))
    return tests


class NumpySummerTestCase(TestCase):
    def test_is_nd_array_list(self):
        with self.assertRaises(TypeError) as e:
            mas_summer(a=np.ndarray([[11, 22], [33, 44]]), b=np.ndarray([[55, 66], [77, 88]]))
        self.assertEqual('\'list\' object cannot be interpreted as an integer', e.exception.args[0])


if __name__ == '__main__':
    main()
