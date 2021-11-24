from unittest import TestCase, main
from tested.first_and_last_package import first_and_last
from tested.first_and_last_package.first_and_last import word_finder
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(first_and_last))
    return tests


class RegTest(TestCase):
    def test_works(self):
        self.assertEqual(
            word_finder(text_str='То,оно,  которое (задание), само себя не сделает'), [('оно', 'о')])

    def test_empty_string(self):
        with self.assertRaises(TypeError) as e:
            word_finder(text_str='')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_string_of_digs(self):
        with self.assertRaises(TypeError) as e:
            word_finder(text_str=1234)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_no_such_word(self):
        self.assertEqual(word_finder(
            text_str=' Дана строка. Найти в этой строке слова, которые начинаються и оканчиваються на одну и ту '), [])

    def test_masked_digs(self):
        with self.assertRaises(TypeError) as e:
            word_finder(text_str='То,оно,  которое (задание), само себя не сделает123')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
