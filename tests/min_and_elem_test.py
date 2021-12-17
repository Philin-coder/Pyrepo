from unittest import TestCase, main
from tested.min_and_elem_package import min_and_elem
from tested.min_and_elem_package.min_and_elem import mass_gen
import doctest
import random


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(min_and_elem))
    return tests


class MinAndElemTest(TestCase):
    def test_is_random_int(self):
        self.assertTrue(1 <= (random.randint(1, 10) <= 10) is True, 'не рандом')

    def test_ret_list_int(self):
        self.assertIsInstance(mass_gen(n=12), list)

    def test_mass_gen_wrong(self):
        with self.assertRaises(TypeError) as e:
            mass_gen(n='12')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
