from unittest import TestCase, main, skipUnless
from tested.shell_comand_package import sheler
from tested.shell_comand_package.sheler import shell_commander
import doctest
import sys


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sheler))
    return tests


class MyTestShell(TestCase):
    @skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_works(self):
        self.assertEqual(shell_commander(text_str='ping ya.ru'), 'command done')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            shell_commander(text_str=123)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
