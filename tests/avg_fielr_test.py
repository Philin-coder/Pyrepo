from unittest import TestCase, main
from tested.avg_in_file_package import avg_filer
from tested.avg_in_file_package.avg_filer import int_list_gen
from tested.avg_in_file_package.avg_filer import write_to_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(avg_filer))
    return tests


class AvgFilerTest(TestCase):
    def test_ints_input(self):
        self.assertEqual(int_list_gen(n=10),
                         [1.0, 1.148698354997035, 1.3903891703159095, 1.7411011265922482, 2.23606797749979,
                          2.9301560515835217, 3.904528777122722, 5.278031643091578, 7.224674055842077,
                          10.000000000000002])

    def test_ints_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            int_list_gen(n='10')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def file_created(self):
        self.assertEqual(write_to_file(file_name='test', f_ext='txt', data_lst=int_list_gen(n=10)), 'file_created')

    def test_wrong_file_create(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(file_name='test', f_ext='tt', data_lst=int_list_gen(n=10))
        self.assertEqual('Файл имеет неверное расширение, либо - передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
