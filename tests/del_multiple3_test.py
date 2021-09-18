from unittest import TestCase, main
from tested.del_multipl_tree_ind_package import del_multipl
from tested.del_multipl_tree_ind_package.del_multipl import del_index
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(del_multipl))
    return tests


class DelMulest(TestCase):
    def test_del_index_even(self):
        self.assertEqual(del_index(input_text_string='горе'), 'ор')

    def test_del_index_odd(self):
        self.assertEqual(del_index(input_text_string='горемыка'), 'ормыа')

    def test_del_index_eng(self):
        self.assertEqual(del_index(input_text_string='hold Fast'), 'ol Fst')

    def test_del_index_int(self):
        with self.assertRaises(TypeError) as e:
            del_index(input_text_string=1)
        self.assertEqual('Введена не строка', e.exception.args[0])


if __name__ == '__main__':
    main()
