from unittest import TestCase, main
from tested.another_class_package import class_mod
from tested.another_class_package.class_mod import Employee
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(class_mod))
    return tests


class SimpleClassTest(TestCase):
    def setUp(self):
        self.em = Employee('John', 222, 222.2, 2)

    def test_name(self):
        self.assertEqual(self.em.name, 'John', 'Значение не является строки john')

    def test_nom(self):
        self.assertEqual(self.em.nom, 222, 'Значение не является числом  222')

    def test_zp(self):
        self.assertEqual(self.em.zp, 222.2, 'Значение не является числом  222.2')

    def test_u_der(self):
        self.assertEqual(self.em.u_der, 2, 'Значение не является числом  2')

    def test_what_name(self):
        self.assertIsInstance(self.em.name, str, 'Значение не строка')

    def test_what_nom(self):
        self.assertIsInstance(self.em.nom, int, 'Значение не целое число')

    def test_what_zp(self):
        self.assertIsInstance(self.em.zp, float, 'Значение не вещественноее число')

    def test_what_u_der(self):
        self.assertIsInstance(self.em.u_der, int, 'Значение не целое  число')

    def test_type_str(self):
        self.assertIsInstance(self.em.printer().__str__(), str, 'Значение является строкой ')


if __name__ == '__main__':
    main()
