from unittest import TestCase, main
from tested.again_sim_func_package import simp_f
from tested.again_sim_func_package.simp_f import func
from tested.again_sim_func_package.simp_f import func2
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(simp_f))
    return tests


class FunTest(TestCase):
    def test_works_int(self):
        self.assertEqual(func2(func(a=2, b=5)), 7)

    def test_works_str(self):
        self.assertEqual(func2(func(a='hello', b='world')), 'helloworld')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            func2(func(a=[1], b=[2]))
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
