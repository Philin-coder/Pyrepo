from unittest import TestCase, main
from tested.happy_ticket_package import happy_ticket
from tested.happy_ticket_package.happy_ticket import happy_ticket_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(happy_ticket))
    return tests


class HappyTickerTest(TestCase):
    def test_string_in_input_happy(self):
        self.assertEqual(happy_ticket_func(text_str='123321'), 'Счастливый')

    def test_string_in_input_uisally(self):
        self.assertEqual(happy_ticket_func(text_str='114111'), 'Обычный')

    def test_string_in_input_empty_str(self):
        with self.assertRaises(TypeError) as e:
            happy_ticket_func(text_str='')
        self.assertEqual('введите строку(номер билета 6 знаков)', e.exception.args[0])

    def test_digs_in_input(self):
        with self.assertRaises(TypeError) as e:
            happy_ticket_func(text_str=1)
        self.assertEqual('введите строку(номер билета 6 знаков)', e.exception.args[0])


if __name__ == '__main__':
    main()
