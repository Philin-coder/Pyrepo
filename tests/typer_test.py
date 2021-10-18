from unittest import TestCase, main
from tested.typer_package import typer
from tested.typer_package.typer import m_typ
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(typer))
    return tests


class TypTest(TestCase):
    def test_works(self):
        self.assertEqual(m_typ('1', '2', '4'), -6)

    def test_wrong(self):
        with self.assertRaises(TypeError) as e:
            m_typ(1, 2, 4)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
