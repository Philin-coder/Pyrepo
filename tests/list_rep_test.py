from unittest import TestCase, main
from tested.word_repeater_package import list_rep_counter
from tested.word_repeater_package.list_rep_counter import list_rep_counter_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(list_rep_counter))
    return tests


class LIstRepTest(TestCase):
    def test_works(self):
        self.assertEqual(list_rep_counter_func(wordlist=['Bob', 'Alice', 'Jane', 'Bob', 'Alice']),
                         {'Bob': 2, 'Alice': 2})

    def test_emty_list(self):
        with self.assertRaises(TypeError) as e:
            list_rep_counter_func(wordlist=[])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_int_in_list(self):
        with self.assertRaises(TypeError) as e:
            list_rep_counter_func(wordlist=['1', 'Alice', 'Jane', 'Bob', 'Alice'])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
