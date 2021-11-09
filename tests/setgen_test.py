from unittest import TestCase, main
from tested.another_set_gen_package import s_gen
from tested.another_set_gen_package.s_gen import tuple_gen_func
from tested.another_set_gen_package.s_gen import tuple_merger
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(s_gen))
    return tests


class MySGenTest(TestCase):
    def test_tuple_gen_func_right(self):
        self.assertEqual(tuple_gen_func(start_p=1, end_p=4), (1, 2, 3, 4))

    def test_tuple_gen_func_wrong(self):
        with self.assertRaises(TypeError) as e:
            tuple_gen_func(start_p='5', end_p='8')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_tuple_merger_is_set(self):
        self.assertIsInstance(
            tuple_merger(t1=tuple_gen_func(start_p=1, end_p=4), t2=tuple_gen_func(start_p=5, end_p=8)), set)


if __name__ == '__main__':
    main()
