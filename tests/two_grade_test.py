from unittest import TestCase, main
from tested.two_grade_package import two_grade
from  tested.two_grade_package.two_grade import check2rec
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(two_grade))
    return tests


class TwoGradeTest(TestCase):
    def test_two_grad_true(self):
        self.assertEqual(check2rec(num=2), True)

    def test_two_grad_false(self):
        self.assertEqual(check2rec(num=122), False)

    def test_ints_in_input(self):
        with self.assertRaises(TypeError) as e:
            check2rec(num='2')
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
