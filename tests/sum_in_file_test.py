from unittest import TestCase, main
from tested.sum_in_file_package import sumer_file
from tested.sum_in_file_package.sumer_file import range_gen
from tested.sum_in_file_package.sumer_file import str_maper
from tested.sum_in_file_package.sumer_file import file_writer
from tested.sum_in_file_package.sumer_file import sum_ints_in_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sumer_file))
    return tests


class SumInFileTest(TestCase):
    def test_range_gen_ints_in_input(self):
        self.assertEqual(range_gen(start_p=1, end_p=10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_range_gen_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            range_gen(start_p='1', end_p='10')
        self.assertEqual('введите числа', e.exception.args[0])

    def test_str_maper_list_in_input(self):
        self.assertEqual(str_maper(m_data=range_gen(start_p=1, end_p=10)), '1 2 3 4 5 6 7 8 9 10')

    def test_str_maper_str_in_input(self):
        with self.assertRaises(TypeError) as e:
            str_maper(m_data=str(range_gen(start_p=1, end_p=10)))
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_file_create(self):
        self.assertEqual(
            file_writer(filename='test', f_ext='txt', w_data=str_maper(m_data=range_gen(start_p=1, end_p=4))),
            'file_created')

    def test_file_create_wrong(self):
        with self.assertRaises(TypeError) as e:
            file_writer(filename='test', f_ext='tt', w_data=str_maper(m_data=range_gen(start_p=1, end_p=4)))
        self.assertEqual('Файл имеет неверный тип', e.exception.args[0])

    def test_sum_ints_in_file(self):
        self.assertEqual(sum_ints_in_file(file_name='test', f_ext='txt'), 10)

    def test_sum_ints_in_fil_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            sum_ints_in_file(file_name='test', f_ext='tt')
        self.assertEqual('Это не файл', e.exception.args[0])


if __name__ == '__main__':
    main()
