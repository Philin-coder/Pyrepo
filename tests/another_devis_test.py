from unittest import TestCase, main
from tested.devs_package import dev_mod
from tested.devs_package.dev_mod import devs
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dev_mod))
    return tests


class AnotherDevsTest(TestCase):
    def test_works(self):
        self.assertEqual(devs(a=1, b=14, n=2),
                         [1, 2, 1, 3, 1, 2, 4, 1, 5, 1, 2, 3, 6, 1, 7, 1, 2, 4, 8, 1, 3, 9, 1, 2, 5, 10, 1, 11, 1,
                          2, 3, 4, 6, 12, 1, 13, 1, 2, 7, 14])

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            devs(a='1', b='14', n='2')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
