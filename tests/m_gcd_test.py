from unittest import TestCase, main
from tested.m_gcd_package import m_gcd
from tested.m_gcd_package.m_gcd import m_gcd_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(m_gcd))
    return tests


class MGcdTest(TestCase):
    def test_int_input(self):
        self.assertEqual(m_gcd_func(a=14, b=21), 42)

    def test_zero_input(self):
        with self.assertRaises(TypeError) as e:
            m_gcd_func(a=0, b=0)
        self.assertEqual('Введите 2 целых подложительных числа', e.exception.args[0])

    def test_char_input(self):
        with self.assertRaises(TypeError) as e:
            m_gcd_func(a='12', b='12')
        self.assertEqual('Введите 2 целых подложительных числа', e.exception.args[0])


if __name__ == '__main__':
    main()
