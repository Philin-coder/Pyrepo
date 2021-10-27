from unittest import TestCase, main
from tested.procentil_package import proc
from tested.procentil_package.proc import porc_func
import doctest
import random


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(proc))
    return tests


class MyProcTest(TestCase):
    def test_is_int(self):
        self.assertIsInstance(random.randint(1, 10), int)

    def test_is_rnd_int(self):
        self.assertTrue((1 <= random.randint(1, 10) <= 10) is True, 'не в диапазоне')

    def test_is_float(self):
        self.assertIsInstance(random.uniform(1, 0), float)

    def test_is_rnd_float(self):
        self.assertTrue((0.0 <= random.uniform(1, 0) <= 1.0) is True, 'не в диапазоне')

    def test_wrong_input_p(self):
        with self.assertRaises(TypeError) as e:
            porc_func(uni_ints=[random.randint(1, 10) for _ in range(10)], p='f')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_wrong_input_set(self):
        with self.assertRaises(TypeError) as e:
            porc_func(uni_ints={random.randint(1, 10) for _ in range(10)}, p=random.uniform(0, 1))
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_wrong_input_emp_list(self):
        with self.assertRaises(TypeError) as e:
            porc_func(uni_ints={random.randint(1, 10) for _ in range(10)}, p=random.uniform(0, 1))
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
