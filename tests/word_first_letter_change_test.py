from unittest import TestCase, main
from  tested.m_word_first_letter_change_package import changer
from  tested.m_word_first_letter_change_package.changer import changer_word_first_letters_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(changer))
    return tests


class WordFirstLetterChangeTest(TestCase):
    def test_change_russian(self):
        self.assertEqual(changer_word_first_letters_func(text_str='Мама мыла раиу'), 'Ммр')

    def test_change_english(self):
        self.assertEqual(changer_word_first_letters_func(text_str='Peace abd love'), 'Pal')

    def test_change_nothing(self):
        with self.assertRaises(TypeError) as e:
            changer_word_first_letters_func(text_str='')
        self.assertEqual('Введите  непустую  строку',e.exception.args[0])

    def test_change_digit(self):
        with self.assertRaises(TypeError) as e:
            changer_word_first_letters_func(text_str=1)
        self.assertEqual('Введите  непустую  строку', e.exception.args[0])

    def test_change_mask_digit(self):
        with self.assertRaises(TypeError) as e:
            changer_word_first_letters_func(text_str='1123 123')
        self.assertEqual('Введите  непустую  строку', e.exception.args[0])


if __name__ == '__main__':
    main()
