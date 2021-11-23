from unittest import TestCase, main
from tested.Pocker_package import poker
from tested.Pocker_package.poker import check_combination
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(poker))
    return tests


class PokerTest(TestCase):
    def test_combination_is_str(self):
        self.assertIsInstance(check_combination([1, 1, 1, 1, 1]), str)

    def test_check_imp(self):
        self.assertEqual(check_combination([1, 1, 1, 1, 1]), 'Impossible')

    def test_four_kind(self):
        self.assertEqual(check_combination([1, 1, 1, 1, 0]), 'Four of a Kind')

    def test_Full_House(self):
        self.assertEqual(check_combination([1, 1, 1, 2, 2]), 'Full House')

    def test_straight(self):
        self.assertEqual(check_combination([1, 2, 3, 4, 5]), 'Straight')

    def test_straight_again(self):
        self.assertEqual(check_combination([1, 5, 3, 2, 4]), 'Straight')

    def test_three_kind(self):
        self.assertEqual(check_combination([1, 1, 1, 2, 4]), 'Three of a Kind')

    def test_two_pair(self):
        self.assertEqual(check_combination([1, 1, 2, 2, 4]), 'Two Pairs')

    def test_one_pair(self):
        self.assertEqual(check_combination([1, 1, 2, 3, 4]), 'One Pair')

    def test_nothing(self):
        self.assertEqual(check_combination([1, 9, 2, 3, 4]), 'Nothing')

    def test_wrong_list(self):
        with self.assertRaises(TypeError) as e:
            check_combination([1, 9, 2, 3, 'f'])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_empty_list(self):
        with self.assertRaises(TypeError) as e:
            check_combination([])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_not_list(self):
        with self.assertRaises(TypeError) as e:
            check_combination({1, 9, 2, 3, 4})
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
