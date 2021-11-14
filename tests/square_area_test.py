from unittest import TestCase, main
from tested.squre_area_package import area_finder
from tested.squre_area_package.area_finder import Square, Rect
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(area_finder))
    return tests


class SquareAreaTest(TestCase):
    def setUp(self):
        self.sq = Square(size=2)
        self.sq_wrong = Square(size='2')
        self.rt = Rect(dl=2, sh=3)
        self.rt_wrong = Rect(dl='2', sh='3')

    def test_is_dl_int(self):
        self.assertIsInstance(self.rt.dl, int, 'Не число ')

    def test_is_sh_int(self):
        self.assertIsInstance(self.rt.sh, int, 'не число')

    def test_rt_area_is_int(self):
        self.assertIsInstance(self.rt.area(), int, 'не число')

    def test_sq_area_is_int(self):
        self.assertIsInstance(self.sq.area(), int, 'не число')

    def test_sq_area(self):
        self.assertEqual(self.sq.area(), 4)

    def test_sq_area(self):
        self.assertEqual(self.rt.area(), 6)

    def test_sq_wrong(self):
        with self.assertRaises(TypeError) as e:
            self.sq_wrong.area()
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_rt_wrong(self):
        with self.assertRaises(TypeError) as e:
            self.rt_wrong.area()
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_rt_printer_is_str(self):
        self.assertIsInstance(self.rt.__str__(), str)

    def test_rt_repr_is_str(self):
        self.assertIsInstance(self.rt.__repr__(), str)

    def test_repr_dl_is_str(self):
        self.assertIsInstance(self.rt.repr_dl(), str)

    def test_repr_sh_is_str(self):
        self.assertIsInstance(self.rt.repr_sh(), str)

    def test_repr_sh(self):
        self.assertEqual(self.rt.repr_sh(), 'ширина фигуры= 3 ')

    def test_rep_dl(self):
        self.assertEqual(self.rt.repr_dl(), 'длинна фигуры= 2 ')

    def test_inheritance_classes(self):
        self.assertTrue(issubclass(Square, Rect) is True, 'Классы не наследуются')

    def test_inheritance_methods(self):
        self.assertTrue(isinstance(Square(size=2), Rect) is True, 'методы не наследуются')


if __name__ == '__main__':
    main()
