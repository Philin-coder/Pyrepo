from unittest import TestCase, main
from tested.even_ints_in_file_package import even_in_file
from tested.even_ints_in_file_package.even_in_file import even_cont_gen
from tested.even_ints_in_file_package.even_in_file import write_to_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(even_in_file))
    return tests


class EvenInFileTest(TestCase):
    def test_cont_gen_int_in_input(self):
        self.assertEqual(even_cont_gen(n=12), [2, 4, 6, 8, 10, 12])

    def test_cont_gen_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            even_cont_gen(n='12')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_file_create(self):
        self.assertEqual(write_to_file(filename='test', f_ext='txt', f_data=even_cont_gen(n=12)), 'file_created')

    def test_wrong_file_create(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(filename='test', f_ext='fxt', f_data=even_cont_gen(n=12))
        self.assertEqual('Файл имеет неверное расширение, или получен неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
