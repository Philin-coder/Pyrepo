from unittest import TestCase, main
from tested.double_multepl_pack import mult
from tested.double_multepl_pack.mult import mul_sum
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mult))
    return tests


class MultTest(TestCase):
    def test_mult_3(self):
        self.assertEqual(mul_sum(x=12, a=12), 'Кратно 3')

    def test_mult_a(self):
        self.assertEqual(mul_sum(x=62, a=2), 'Кратно a')

    def test_not_mult_any(self):
        self.assertEqual(mul_sum(x=16, a=3), 'число не кратно не 3  не а ')

    def test_not_one_sign(self):
        self.assertEqual(mul_sum(x=9, a=3), 'Число не двузначное')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            mul_sum(x='9', a=3)
        self.assertEqual('Введите числа', e.exception.args[0])


if __name__ == '__main__':
    main()
