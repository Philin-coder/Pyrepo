from unittest import TestCase, main
from tested.graphic_pacage import graphick
from tested.graphic_pacage.graphick import graph
import  doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(graphick))
    return tests


class graphickTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(graph(x=0, y=-2), -2.0)

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            graph('12', '23')
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
