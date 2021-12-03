from unittest import TestCase, main
from avg_pack import ager
from tested.avg_pack.ager import cont_gen
from tested.avg_pack.ager import write_to_file
from tested.avg_pack.ager import read_from_file
from tested.avg_pack.ager import conv_to_int
from tested.avg_pack.ager import avg_of_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(ager))
    return tests


class MyAvgTest(TestCase):
    def test_cont_gen_right(self):
        self.assertEqual(cont_gen(n=8), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_cont_gen_wrong(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(n='8')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_write_file_right(self):
        self.assertEqual(write_to_file(file_name='avg_file', f_ext='txt', f_data=cont_gen(n=8)), 'file_created')

    def test_write_file_wrong(self):
        with self.assertRaises(ValueError) as e:
            write_to_file(file_name='avg_file', f_ext='tx', f_data=cont_gen(n=8))
        self.assertEqual('файл имеет неверный тип', e.exception.args[0])

    def test_read_file_right(self):
        self.assertEqual(read_from_file(file_name='avg_file', f_ext='txt'), ['[1, 2, 3, 4, 5, 6, 7, 8]\n'])

    def test_read_file_wrong(self):
        with self.assertRaises(FileNotFoundError) as e:
            read_from_file(file_name='avg_file', f_ext='tx')
        self.assertEqual('нет такого файла', e.exception.args[0])

    def test_conv_to_int_right(self):
        self.assertEqual(conv_to_int(fdata=read_from_file(file_name='avg_file', f_ext='txt')), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_conv_to_int_wrong(self):
        with self.assertRaises(TypeError) as e:
            conv_to_int(fdata=None)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_avg_of_file_wrong(self):
        with self.assertRaises(TypeError) as e:
            avg_of_file(avg_data=conv_to_int(fdata={}))
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_avg_of_file_right(self):
        self.assertEqual(avg_of_file(avg_data=conv_to_int(fdata=read_from_file(file_name='avg_file', f_ext='txt'))),
                         4.5)

    def test_avg_of_file_zero_div(self):
        with self.assertRaises(ZeroDivisionError) as e:
            avg_of_file(avg_data=[])
        self.assertEqual('на ноль делить грешно ',e.exception.args[0])




if __name__ == '__main__':
    main()
