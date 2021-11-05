from unittest import TestCase, main
from tested.another_file_creator_package import file_creator
from tested.another_file_creator_package.file_creator import cont_gen
from tested.another_file_creator_package.file_creator import file_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(file_creator))
    return tests


class FileCreateTest(TestCase):
    def test_wrong_input_gen_cont(self):
        self.assertEqual((cont_gen(data='test')), 'test')

    def test_wrong_input_gen_cont(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(data=123)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_file_create(self):
        with self.assertRaises(ValueError) as e:
            file_gen(my_f_name='test', f_ext='t', f_data=cont_gen(data='ПРОба2'))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])


if __name__ == '__main__':
    main()
