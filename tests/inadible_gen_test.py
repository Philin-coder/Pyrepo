from unittest import TestCase, main
from tested.inaudible_gen_package import inaudible_gen
from tested.inaudible_gen_package.inaudible_gen import inaudible_gen_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(inaudible_gen))
    return tests


class InGEnTest(TestCase):
    def test_works(self):
        self.assertEqual(inaudible_gen_func(letters='аиеёэоуыэяюАЁИЮЭЫУЕОЯ.,!?-;:', words='Удивительный факт, но'),
                         'двтльнй фкт н')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            inaudible_gen_func(letters=1, words=1)
        self.assertEqual('Введены не строки', e.exception.args[0])


if __name__ == '__main__':
    main()
