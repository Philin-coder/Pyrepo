from unittest import TestCase, main
from tested.file_example_package import file_example
from tested.file_example_package.file_example import generate_cont
from tested.file_example_package.file_example import write_to_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(file_example))
    return tests


class FileTestWrite(TestCase):
    def test_right_data(self):
        self.assertEqual(generate_cont(data_str='yes'), 'yes')

    def test_wrong_data(self):
        with self.assertRaises(TypeError) as e:
            generate_cont(data_str='')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_file_create(self):
        self.assertEqual(write_to_file(filename='test', f_ext='txt', f_data=generate_cont(data_str='yes')),
                         'file_created')

    def test_wrong_file_create(self):
        with self.assertRaises(TypeError) as e:
            write_to_file(filename='test', f_ext='fxt', f_data=generate_cont(data_str='yes'))
        self.assertEqual('файл имеет неверное расширение', e.exception.args[0])


if __name__ == '__main__':
    main()
