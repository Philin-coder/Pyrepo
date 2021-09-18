from unittest import TestCase, main
from tested.all_input_paxkage import inputer
from tested.all_input_paxkage.inputer import changer
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(inputer))
    return tests


class All_inputTest(TestCase):
    def test_it_workd(self):
        self.assertEqual(changer(text_str='Самая длинная река это Волга', text_substr='Волга',
                                 repl_str='Нил'), 'Самая длинная река это Нил')

    def test_wrong_input(self):
        with self.assertRaises(ValueError) as e:
            changer(text_str=14, text_substr=234,repl_str=1)
        self.assertEqual('Проверьте, возможно, введена не строка ',e.exception.args[0])

    def test_empty_input(self):
        with self.assertRaises(ValueError) as e:
            changer(text_str='', text_substr='', repl_str='')
        self.assertEqual('Проверьте, возможно, введена не строка ', e.exception.args[0])

    def test_list_input(self):
        with self.assertRaises(ValueError) as e:
            changer(text_str=[123], text_substr=[123], repl_str=[123])
        self.assertEqual('Проверьте, возможно, введена не строка ', e.exception.args[0])

if __name__ == '__main__':
    main()
