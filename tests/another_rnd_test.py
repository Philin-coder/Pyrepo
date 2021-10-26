from unittest import TestCase, main
from tested.another_random_package import randomer
from tested.another_random_package.randomer import my_rand
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(randomer))
    return tests


class MyRndTestTest(TestCase):
    def test_is_int(self):
        self.assertIsInstance(my_rand(start_p=1, end_p=10), int)

    def test_is_rand_int(self):
        self.assertTrue((1 <= my_rand(start_p=1, end_p=10) <= 10) is True, 'не рандом ')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            my_rand(start_p='1', end_p='1')
        self.assertEqual('Введите  целые числа', e.exception.args[0])


if __name__ == '__main__':
    main()
