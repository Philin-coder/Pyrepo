import doctest
from unittest import TestCase, main

from tested.russian_vowels_in_str import rus_wolwes_in_str
from tested.russian_vowels_in_str.rus_wolwes_in_str import rus_w_lister


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(rus_wolwes_in_str))
    return tests


class RusWolInStrTest(TestCase):
    def test_c(self):
        self.assertEqual(rus_w_lister('ПРОбуй и получится'), 6)

    def test_normal_letter(self):
        self.assertEqual(rus_w_lister('привет, мир'), 3)

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(rus_w_lister(12))
        self.assertEqual('Необходимо вводить строки, не числа', e.exception.args[0])

    if __name__ == '__main__':
        main()
