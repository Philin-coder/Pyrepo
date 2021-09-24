from unittest import TestCase, main
from tested.set_package import set_checker
from tested.set_package.set_checker import set_enq_func
from tested.set_package.set_checker import subset_test_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(set_checker))
    return tests


class SetTest(TestCase):
    def test_set_not_equal(self):
        self.assertEqual(set_enq_func(text_str='123', text_str2='12'), 'множества  не равны')

    def test_set_equal(self):
        self.assertEqual(set_enq_func(text_str='123', text_str2='123'), 'множества равны')

    def test_subset_True(self):
        self.assertEqual(subset_test_func(text_str='3', text_str2='123'), True)

    def test_subset_False(self):
        self.assertEqual(subset_test_func(text_str='0', text_str2='123'), False)

    def test_set_enq_wrong(self):
        with self.assertRaises(TypeError) as e:
            set_enq_func(text_str=123, text_str2=123)
        self.assertEqual('введите 2 строки', e.exception.args[0])

    def test_set_subset_wrong(self):
        with self.assertRaises(TypeError) as e:
            subset_test_func(text_str=123, text_str2=12)
        self.assertEqual('Введите 2 строки', e.exception.args[0])


if __name__ == '__main__':
    main()
