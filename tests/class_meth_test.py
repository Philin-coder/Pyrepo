from unittest import TestCase, main
from tested.class_poperty_and_method_package import class_meh
from tested.class_poperty_and_method_package.class_meh import Stud
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(class_meh))
    return tests


class MethTest(TestCase):
    def setUp(self):
        self.st = Stud(name='Петр ', nickname='Ger Petter')
        self.sl = Stud(name='Павел ', nickname='Apostol')

    def test_name_st(self):
        self.assertEqual(self.st.name, 'Петр ', 'Значение не является  строкой Петр')

    def test_nickname_st(self):
        self.assertEqual(self.st.nickname, 'Ger Petter', 'Значение не является  строкой Ger Petter')

    def test_what_is_name_st(self):
        self.assertIsInstance(self.st.name, str, 'не строка')

    def test_what_is_nickname_st(self):
        self.assertIsInstance(self.st.nickname, str, 'не строка')

    def test_name_sl(self):
        self.assertEqual(self.sl.name, 'Павел ', 'Значение не является  строкой Павел')

    def test_nick_name_sl(self):
        self.assertEqual(self.sl.nickname, 'Apostol', 'Значение не является  строкой Apostol')

    def test_Stud_mul_three_st(self):
        self.assertEqual(self.st.name_mul_three(self.st.name), 'Петр Петр Петр ')

    def test_Stud_mul_three_type_st(self):
        self.assertIsInstance(self.st.name_mul_three(self.st.name), str, 'не строка')

    def test_Stud_nick_name_generator_st(self):
        self.assertEqual(self.st.nick_name_generator, 'Петр  Ger Petter')

    def test_Stud_nick_name_generator_type_st(self):
        self.assertIsInstance(self.st.nick_name_generator, str, 'не строка')


if __name__ == '__main__':
    main()
