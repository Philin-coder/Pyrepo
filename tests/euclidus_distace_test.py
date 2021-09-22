from unittest import TestCase, main
from tested.euclidus_dist_paxkage import euclidus_distance
from tested.euclidus_dist_paxkage.euclidus_distance import euclidean_distance_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(euclidus_distance))
    return tests


class DistTest(TestCase):
    def test_normal_input(self):
        self.assertEqual(euclidean_distance_func(v1=[12.0, 11.0, 2], v2=[11.0, 9.0, 1.0]), 2.449489742783178)

    def test_one_float_input(self):
        self.assertEqual(euclidean_distance_func(v1=[12.0], v2=[11.0]), 1.0)

    def test_mut_nput(self):
        self.assertEqual(euclidean_distance_func(v1=[12.0], v2=[11.0]), 1.0)

    def test_not_list_input(self):
        with self.assertRaises(TypeError) as e:
            euclidean_distance_func(v1=(12.0), v2=[11.0, 1112, 4])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_char_first_list_input(self):
        with self.assertRaises(TypeError) as e:
            euclidean_distance_func(v1=[12.0, '1'], v2=[11.0, 1112, 4])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_char_second_list_input(self):
        with self.assertRaises(TypeError) as e:
            euclidean_distance_func(v1=[12.0], v2=['@', 11.0, 1112, 4])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
