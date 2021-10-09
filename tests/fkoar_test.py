from unittest import TestCase, main
from tested.floor_package import floorer
from tested.floor_package.floorer import floors
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(floorer))
    return tests


class FloorTest(TestCase):
    def test_works(self):
        self.assertEqual(floors(n=7), 'Time is :56.284016906250024')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            floors(n='7')
        self.assertEqual('введено не число', e.exception.args[0])


if __name__ == '__main__':
    main()
