from unittest import TestCase, main
from tested.nums_only_in_file_package import nums_in_file
from tested.nums_only_in_file_package.nums_in_file import cont_gen
from tested.nums_only_in_file_package.nums_in_file import write_file
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(nums_in_file))
    return tests


class Test(TestCase):
    def test_right_input_gen_cont(self):
        self.assertEqual(cont_gen(text_str='1s2t3o4p'), [1, 2, 3, 4])

    def test_wrong_input_gen_cont(self):
        with self.assertRaises(TypeError) as e:
            cont_gen(text_str={'1s2t3o4p'})
        self.assertEqual('Передан  неверный тип данных', e.exception.args[0])

    def test_write_file(self):
        self.assertEqual(write_file(file_name='test', f_ext='txt', ls_data=cont_gen(text_str='1s2t3o4p')),
                         'file_created')

    def test_wrong_write_file(self):
        with self.assertRaises(ValueError) as e:
            write_file(file_name='test', f_ext='t', ls_data=cont_gen(text_str='1s2t3o4p'))
        self.assertEqual('Файл имеет неверное расширение', e.exception.args[0])


if __name__ == '__main__':
    main()
