from unittest import TestCase, main
from tested.list_slise_reverse_pacage import list_slice_rev
from tested.list_slise_reverse_pacage.list_slice_rev import int_list_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(list_slice_rev))
    return tests


class list_slise_reverseTest(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(int_list_gen(n=12), [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_chars_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(int_list_gen(n='12'))
        self.assertEqual('Должно быть введено целое, положительное число', e.exception.args[0])

    def test_list_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(int_list_gen(n=[1, 2, 3, 4]))
        self.assertEqual('Должно быть введено целое, положительное число', e.exception.args[0])

    def test_ints_in_input(self):
        self.assertEqual(int_list_gen(n=12), [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_chars_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(int_list_gen(n='12'))
        self.assertEqual('Должно быть введено целое, положительное число', e.exception.args[0])

    def test_list_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(int_list_gen(n=[1, 2, 3, 4]))
        self.assertEqual('Должно быть введено целое, положительное число', e.exception.args[0])

    def test_emp_in_input(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(int_list_gen(n=''))
        self.assertEqual('Должно быть введено целое, положительное число', e.exception.args[0])


if __name__ == '__main__':
    main()
