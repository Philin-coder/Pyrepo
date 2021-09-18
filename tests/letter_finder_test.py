from unittest import TestCase, main
from tested.letter_finder_package import letter_finder
from tested.letter_finder_package.letter_finder import finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(letter_finder))
    return tests


class LetterFinderTest(TestCase):
    def test_all_letters(self):
        self.assertEqual(finder(text_str='мир'), True)

    def test_all_lett_av(self):
        self.assertEqual(finder(text_str='рим'), True)

    def test_one_letter(self):
        self.assertEqual(finder(text_str='тип'), False)

    def test_no_one_letter(self):
        self.assertEqual(finder(text_str='кот'), False)

    def test_empty_str(self):
        with self.assertRaises(ValueError) as e:
            finder(text_str='')
        self.assertEqual('Cтрока пуста', e.exception.args[0])

    def test_int_in_str(self):
        with self.assertRaises(TypeError) as e:
            finder(text_str=1)
        self.assertEqual('Необходимо вводить не пустую строку', e.exception.args[0])

        if __name__ == '__main__':
            main()
