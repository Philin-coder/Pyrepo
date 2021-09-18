from unittest import TestCase, main
from tested.commmon_lettet_package import common_letter
from tested.commmon_lettet_package.common_letter import most_common_english_letter
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(common_letter))
    return tests


class LatterTest(TestCase):
    def test_most_common_letter_works(self):
        self.assertEqual(most_common_english_letter(text_str='test list fast'), 't')

    def test_most_common_letter_works_rus(self):
        with self.assertRaises(TypeError) as e:
            most_common_english_letter(text_str='проба')
        self.assertEqual('Введите строку на английском ',e.exception.args[0])

    def test_most_common_letter_works_digits(self):
        with self.assertRaises(TypeError) as e:
            most_common_english_letter(text_str=1)
        self.assertEqual('не вводить цифры', e.exception.args[0])


if __name__ == '__main__':
    main()
