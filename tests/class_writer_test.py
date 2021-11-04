from unittest import TestCase, main
from tested.wrie_to_fiel_class_package import class_writer
from tested.wrie_to_fiel_class_package.class_writer import Deposit
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(class_writer))
    return tests


class ClassWriterTest(TestCase):
    def setUp(self):
        self.dp = Deposit(naim='Иванов', nom_s=1212, sum_year=12.1, y_r=1997)
        self.dp1 = Deposit(naim='Петров', nom_s=1112, sum_year=11.1, y_r=1998)

    def test_naim_dp(self):
        self.assertEqual(self.dp.naim, 'Иванов', 'Значение не является  строкой Иванов')

    def test_nom_s_dp(self):
        self.assertEqual(self.dp.nom_s, 1212, 'Значение не является  числом 1212')

    def test_sum_year_dp(self):
        self.assertEqual(self.dp.sum_year, 12.1, 'Значение не является  числом 112.1')

    def test_y_r_dp(self):
        self.assertEqual(self.dp.y_r, 1997, 'Значение не является  числом 1997')

    def test_what_is_naim_dp(self):
        self.assertIsInstance(self.dp.naim, str, 'Значение не является  строкой')

    def test_what_is_nom_s_dp(self):
        self.assertIsInstance(self.dp.nom_s, int, 'Значение не является  числом')

    def test_what_is_sum_year_dp(self):
        self.assertIsInstance(self.dp.sum_year, float, 'Значение не является вещественным  числом')

    def test_what_is_sum_y_r_dp(self):
        self.assertIsInstance(self.dp.y_r, int, 'Значение не является   числом')

    def test_deposit_repr(self):
        self.assertIsInstance(self.dp.__repr__(), str, 'Значение не является  строкой')

    def test_gen_cont(self):
        self.assertIsInstance(self.dp.gen_cont(), list)

    def test_gen_cont_test(self):
        self.assertEqual(self.dp.gen_cont(), ['Иванов', 1212, 12.1, 1997])

    def test_write_to_file(self):
        self.assertEqual(self.dp.write_to_file('test', f_ext='txt', ls_data=self.dp.gen_cont()), 'file_created')

    def test_file_reader(self):
        self.assertEqual(self.dp.file_reader(file_name='test', f_ext='txt'), 'file_read')

    def test_gen_cont_is_list(self):
        self.assertTrue(isinstance(self.dp.gen_cont(), list), True)

    def test_write_to_file(self):
        with self.assertRaises(ValueError) as e:
            self.dp.write_to_file('test', f_ext='tt', ls_data=self.dp.gen_cont())
        self.assertEqual('Файл имеет неверное расширение', e.exception.args[0])

    def test_read_file(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.dp.file_reader(file_name='', f_ext='tt')
        self.assertEqual('это  не файл', e.exception.args[0])

    def test_sorting(self):
        with self.assertRaises(TypeError) as e:
            self.dp.sorting(data=None)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
