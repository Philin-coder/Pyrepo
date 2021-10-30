from unittest import TestCase, main
from tested.linar_rec_paxkage import linarer
from tested.linar_rec_paxkage.linarer import lean_rec
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(linarer))
    return tests


class LinRecTest(TestCase):
    def test_works_list_in(self):
        self.assertEqual(lean_rec(lst=[[1, 2], 4, [[2, 4, 8, [-4, "er", [0], [{2: "primer"}], []]]]]),
                         [1, 2, 4, 2, 4, 8, -4, 'er', 0, {2: 'primer'}])

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            lean_rec(lst=lean_rec(lst=([1, 2], 4, [[2, 4, 8, [-4, "er", [0], [{2: "primer"}], []]]])))
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
