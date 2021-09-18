from unittest import TestCase, main
from tested.list_revese_package import list_rev
from tested.list_revese_package.list_rev import list_reverse_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(list_rev))
    return tests


class ListRevTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(list_reverse_gen(n=12), [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_chars_ints_in_input(self):
        with self.assertRaises(ValueError) as e:
            self.assertEqual(list_reverse_gen(n='12'))
        self.assertEqual('Должно быть введено целое, положительное число', e.exception.args[0])

    def test_list_in_input(self):
        with self.assertRaises(ValueError) as e:
            self.assertEqual(list_reverse_gen(n=[1, 2, 3, 4]))
        self.assertEqual('Должно быть введено целое, положительное число', e.exception.args[0])


if __name__ == '__main__':
    main()
