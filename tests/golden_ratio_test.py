from unittest import TestCase, main
from tested.glden_ratio_package import golden
from tested.glden_ratio_package.golden import golden_ratio_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(golden))
    return tests


class RatioTest(TestCase):
    def test_ratio_int(self):
        self.assertEqual(golden_ratio_func(12), 0.38197424892703863)

    def test_ratio_cHCAR(self):
        with self.assertRaises(TypeError) as e:
            golden_ratio_func('12')
        self.assertEqual('Введите число', e.exception.args[0])


if __name__ == '__main__':
    main()
