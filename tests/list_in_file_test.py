from unittest import TestCase, main
from tested.list_in_file_paxkage import list_in_file
from tested.list_in_file_paxkage.list_in_file import generate_cont
from tested.list_in_file_paxkage.list_in_file import write_to_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(list_in_file))
    return tests


class ListInFileTest(TestCase):
    def test_right_data(self):
        self.assertEqual(generate_cont(data_lst=[1, 2, 3, 4]), [1, 2, 3, 4])

    def test_wrong_data(self):
        with self.assertRaises(TypeError) as e:
            generate_cont(data_lst={1, 2, 3, 4})
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_file_create(self):
        self.assertEqual(write_to_file(filename='test', f_ext='txt',
                                       f_data=generate_cont(data_lst=[1, 2, 3])), 'file_created')

    def test_wrong_file_create(self):
        with self.assertRaises(TypeError) as e:
            write_to_file(filename='test', f_ext='fxt', f_data=generate_cont(data_lst=[1, 2, 3]))
        self.assertEqual('файл имеет неверное расширение', e.exception.args[0])


if __name__ == '__main__':
    main()
