from unittest import TestCase, main
from tested.method_explorer_package import method_explorer_mod
from tested.method_explorer_package.method_explorer_mod import *
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(method_explorer_mod))
    return tests


class MethExplorerTest(TestCase):
    def setUp(self):
        self.Fr = First()

    def test_my_method_right(self):
        self.assertEqual(self.Fr.my_exm_method(test_str='hello'), 'hello')

    def test_my_method_wrong(self):
        with self.assertRaises(TypeError) as e:
            self.Fr.my_exm_method(test_str=123)
        self.assertEqual('Передан неверный тип данных ', e.exception.args[0])

    def test_class_method_viewer_right(self):
        self.assertTrue((['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
                          '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
                          '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
                          '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
                          'class_method_finder', 'class_method_viewer', 'my_exm_method'] == dir(self.Fr)) is True,
                        'методы в наличии')

    def test_test_class_method_viewer_wrong(self):
        with self.assertRaises(TypeError) as e:
            self.Fr.class_method_viewer(cl_name=None)
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_class_method_finder_right(self):
        self.assertEqual(self.Fr.class_method_finder(dir_list=self.Fr.class_method_viewer(cl_name=First),
                                                     meth_name='my_exm_method'), 'Метод my_exm_method найден')

    def test_class_method_finder_loss(self):
        self.assertEqual(self.Fr.class_method_finder(dir_list=self.Fr.class_method_viewer(cl_name=First),
                                                     meth_name='y_exm_method'), 'Метод y_exm_method  не найден')


if __name__ == '__main__':
    main()
