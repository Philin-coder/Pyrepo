from unittest import TestCase, main
from tested.the_fsrthest_planet_package import f_planet
from tested.the_fsrthest_planet_package.f_planet import find_farthest_orbit
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(f_planet))
    return tests


class PlanetTest(TestCase):
    def test_right(self):
        self.assertEqual(*find_farthest_orbit([(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]), (6, 6))

    def test_wrong(self):
        with self.assertRaises(TypeError) as e:
            find_farthest_orbit(orbits=[(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), 1])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
