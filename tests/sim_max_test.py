from unittest import TestCase, main
from tested.simple_max_package import sim_max
from tested.simple_max_package.sim_max import get_max_sim
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sim_max))
    return tests


class SimMaxTest(TestCase):
    def test_works(self):
        self.assertEqual(get_max_sim(lst=[1, 2, 3, 4]), 4)

    def test_wrong_input_not_list(self):
        with self.assertRaises(TypeError) as e:
            get_max_sim(lst={1, 2, 3, 4})
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_wrong_input_not_ints(self):
        with self.assertRaises(TypeError) as e:
            get_max_sim(lst=['1', '2', '3', '4'])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
