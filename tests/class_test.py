from unittest import TestCase, main
from tested.class_package import inh_class
from tested.class_package.inh_class import Employee, Manager
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(inh_class))
    return tests


class ClassTest(TestCase):
    def setUp(self):
        self.em = Employee('John', 'Smih', 123)
        self.mn = Manager('Ivan', 'Jons', 123, 'Alten')

    def test_naim(self):
        self.assertEqual((self.em.naim), 'John', "Значение не является  строкой John")

    def test_surname(self):
        self.assertEqual((self.em.surname), 'Smih', "Значение не является  строкой Smih")

    def test_pay(self):
        self.assertEqual((self.em.pay), 123, "Значение не является целым строкой  123")

    def test_what_is_naim(self):
        self.assertIsInstance(self.em.naim, str, "Значение не является строкой")

    def test_what_is_surname(self):
        self.assertIsInstance(self.em.surname, str, "Значение не является  строкой")

    def test_what_is_pay(self):
        self.assertIsInstance(self.em.pay, int , "Значение не является числом")

    def test_type_tuple(self):
        self.assertIsInstance(self.em.__str__(), tuple, "Значение не является картежем")

    def test_ineerity(self):
        self.assertTrue(issubclass(Manager, Employee) == True, "не наследуются")

    def test_ineerity_methods(self):
        self.assertTrue(isinstance(Manager('Ivan', 'Jons', 123, 'Alten'), Employee) == True, " Методы не наследуются")

    def test_naim_mn(self):
        self.assertEqual((self.mn.naim), 'Ivan', "Значение не является  строкой Ivan")

    def test_surname_mn(self):
        self.assertEqual((self.mn.surname), 'Jons', "Значение не является  строкой Jons")

    def test_pay_mn(self):
        self.assertEqual((self.mn.pay), 123, "Значение не является  числом 123")

    def test_rank_mn(self):
        self.assertEqual((self.mn.rank), 'Alten', "Значение не является  строкой  Alten")

    def test_what_is_naim_mn(self):
        self.assertIsInstance(self.mn.naim, str, "Значение не является  строкой")

    def test_what_is_surname_mn(self):
        self.assertIsInstance(self.mn.surname, str, "Значение не является  строкой")

    def test_what_is_pay_mn(self):
        self.assertIsInstance(self.mn.pay, str, "Значение не является целым числом")

    def test_what_is_pay_mn(self):
        self.assertIsInstance(self.mn.rank, str, "Значение не является строкой")

    def test_type_tuple_mn(self):
        self.assertIsInstance(self.mn.m_output(), tuple, "Значение не является картежем")


if __name__ == '__main__':
    main()
