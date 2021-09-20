from unittest import TestCase, main
from tested.dict_in_class_package import dict_in_class
from tested.dict_in_class_package.dict_in_class import Employee
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dict_in_class))
    return tests


class DIctClassTest(TestCase):
    def setUp(self):
        self.em = Employee('john', 222, 222.2, 2, 12.2)

    def test_name(self):
        self.assertEqual(self.em.name, 'john', 'Значение не является строкой john')

    def test_nom(self):
        self.assertEqual(self.em.nom, 222, 'Значение не является числом  222')

    def test_zp(self):
        self.assertEqual(self.em.zp, 222.2, 'Значение не является числом  222.2')

    def test_u(self):
        self.assertEqual(self.em.u, 2, 'Значение не является числом  2')

    def test_kom(self):
        self.assertEqual(self.em.kom, 12.2, 'Значение не является числом  12.2')

    def test_what_is_name(self):
        self.assertIsInstance(self.em.name, str, 'Значение не является строкой')

    def test_what_is_nom(self):
        self.assertIsInstance(self.em.nom, int, 'Значение не является целым числом ')

    def test_what_is_zp(self):
        self.assertIsInstance(self.em.zp, float, 'Значение не является вещественным  числом ')

    def test_what_is_u(self):
        self.assertIsInstance(self.em.u, int, 'Значение не является целым   числом ')

    def test_what_is_kom(self):
        self.assertIsInstance(self.em.kom, float, 'Значение не является вещественным   числом ')

    def test_what_in_output(self):
        self.assertIsInstance(self.em.__dict__, dict, 'Метод возвращает  не словарь')

    def test_what_in_returns(self):
        self.assertEqual(self.em.__dict__, {'name': 'john', 'nom': 222, 'zp': 222.2, 'u': 2, 'kom': 12.2})

    def test_what_in_str(self):
        self.assertIsInstance(self.em.__str__(), tuple, 'Значение не является уортежем')

    def test_str(self):
        self.assertEqual(self.em.__str__(), ('Employee:john', 'number 222', 'pay222.2', 'restrict2', 'kom12.2'))


if __name__ == '__main__':
    main()
