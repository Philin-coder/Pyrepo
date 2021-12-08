from unittest import TestCase, main
from tested.guess_num_package import num_gesser
from tested.guess_num_package.num_gesser import guess_number
import doctest
import random


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(num_gesser))
    return tests


class NumGuesserTest(TestCase):
    def test_is_random_int(self):
        self.assertTrue((1 <= random.randint(1, 99) <= 100) is True, 'не рандом')

    def test_var_wrong(self):
        with self.assertRaises(TypeError) as e:
            guess_number(var2='78')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
