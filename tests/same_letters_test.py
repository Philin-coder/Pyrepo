from unittest import TestCase, main
from tested.same_letters_package import same_letters
from tested.same_letters_package.same_letters import first_and_last_let_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(same_letters))
    return tests


class SameLettersTest(TestCase):
    def test_same(self):
        self.assertEqual(first_and_last_let_func(text_str='окно'), 'первая и последняя буквы совпадают')

    def test_not_same(self):
        self.assertEqual(first_and_last_let_func(text_str='окна'), 'первая и последняя буквы не  совпадают')

    def test_not_same_big(self):
        self.assertEqual(first_and_last_let_func(text_str='ОкнО'), 'первая и последняя буквы совпадают')

    def test_not_mask_digit(self):
        with self.assertRaises(TypeError) as e:
            first_and_last_let_func(text_str='1234')
        self.assertEqual('Введите непустую строку в нижнем или верхнем  регистре ', e.exception.args[0])

    def test_empty_str(self):
        with self.assertRaises(TypeError) as e:
            first_and_last_let_func(text_str='')
        self.assertEqual('Введите непустую строку в нижнем или верхнем  регистре ', e.exception.args[0])

    def test_not_digits(self):
        with self.assertRaises(TypeError) as e:
            first_and_last_let_func(text_str=123)
        self.assertEqual('Введите непустую строку в нижнем или верхнем  регистре ', e.exception.args[0])


if __name__ == '__main__':
    main()
