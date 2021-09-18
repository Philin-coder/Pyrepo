from unittest import TestCase, main
import doctest
from tested.my_calc import simple_calc

from tested.my_calc.simple_calc import counter


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(simple_calc))
    return tests


class CounterTest(TestCase):
    def test_plus(self):
        self.assertEqual(counter('+', 2.0, 2.0), 4)

    def test_minus(self):
        self.assertEqual(counter('-', 4.0, 1.0), 3)

    def test_multi(self):
        self.assertEqual(counter('*', 4.0, 3.0), 12)

    def test_div(self):
        self.assertEqual(counter('/', 12.0, 2.0), 6)

    def test_wrong_sign(self):
        with self.assertRaises(ValueError) as e:
            counter('text', 1.0, 2.0)
        self.assertEqual('нет нужных знаков', e.exception.args[0])

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError) as e:
            counter('/', 12.0, 0.0)
        self.assertEqual('На ноль не делим ', e.exception.args[0])


if __name__ == '__main__':
    main()
