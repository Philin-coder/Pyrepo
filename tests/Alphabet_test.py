from unittest import TestCase, main
from tested.Alphabet_package import alphabet
from tested.Alphabet_package.alphabet import alphabetic_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(alphabet))
    return tests


class AlphabetTest(TestCase):
    def test_aski_wromg(self):
        with self.assertRaises(TypeError) as e:
            alphabetic_func(text_str=' ')
        self.assertEqual('Введена не буква', e.exception.args[0])

    def test_aski_ints(self):
        with self.assertRaises(TypeError) as e:
            alphabetic_func(text_str=1)
        self.assertEqual('Введена не буква', e.exception.args[0])

    def test_aski_space(self):
        with self.assertRaises(TypeError) as e:
            alphabetic_func(text_str='')
        self.assertEqual('Введена не буква', e.exception.args[0])




if __name__ == '__main__':
    main()
