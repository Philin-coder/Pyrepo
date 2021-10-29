from unittest import TestCase, main
from tested.summ_more_ten_package import more_ten_smmer
from tested.summ_more_ten_package.more_ten_smmer import sum_more_ten
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(more_ten_smmer))
    return tests


class MoreTenTest(TestCase):
    def test_works(self):
        self.assertEqual(sum_more_ten(ints=[1, 3, 45, 6, 8, 11]), 56)

    def test_wrong_input_not_list(self):
        with self.assertRaises(TypeError) as e:
            sum_more_ten(ints={1, 3, 45, 6, 8, 11})
        self.assertEqual('Передан неверный  тип данных', e.exception.args[0])

    def test_wrong_input_not_ints(self):
        with self.assertRaises(TypeError) as e:
            sum_more_ten(ints=['1', '3', '45', '6', '8', '11'])
        self.assertEqual('Передан неверный  тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
