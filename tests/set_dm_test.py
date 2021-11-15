from unittest import TestCase, main
from tested.setter_demo_package import set_dm
from tested.setter_demo_package.set_dm import Employee
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(set_dm))
    return tests


class SetDmTest(TestCase):
    def setUp(self):
        self.em = Employee("john", "smith", 20.0)
        self.em_wrong = Employee("john", "smith", 120.0)

    def test_name_is_string(self):
        self.assertIsInstance(self.em.name, str)

    def test_name_is_not_empty(self):
        self.assertIsNotNone(self.em.name)

    def test_age_is_digit(self):
        self.assertIsInstance(self.em.age, float)

    def test_age_is_not_zero(self):
        self.assertIsNot(self.em.age, 0, 'Возраст не может быть равен 0')

    def test_age_is_not_negative(self):
        self.assertIsNot(0 < self.em.age, 'Возраст не может быть отрицательным ')

    def test_age_set(self):
        self.assertTrue(1 <= (self.em.age <= 100) is True, 'Возраст указан не верно')

    def test_disp_type(self):
        self.assertIsInstance(self.em.disp(), str)

    def test_val_name(self):
        self.assertTrue((self.em.name == 'john') is True, 'Имя не соответствует')

    def test_val_surname(self):
        self.assertTrue((self.em.surname == 'smith') is True, 'Фамилия  не соответствует')

    def test_val_age(self):
        self.assertTrue((self.em.age == 20) is True, 'Возраст   не соответствует')

    def test_str(self):
        self.assertEqual(self.em.__str__(), 'имя john	,  фамилия smith	 Возраст 20.0	')


if __name__ == '__main__':
    main()
