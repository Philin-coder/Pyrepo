from unittest import TestCase, main
from tested.cube_root_package import cube_roots
from tested.cube_root_package.cube_roots import cube_root_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cube_roots))
    return tests


class CubeRootTest(TestCase):
    def test_cube_root_list(self):
        self.assertEqual(cube_root_func(),
                         [1.0, 1.2599210498948732, 1.4422495703074083, 1.5874010519681994, 1.7099759466766968,
                          1.8171205928321397, 1.912931182772389, 2.0, 2.080083823051904, 2.154434690031884])


if __name__ == '__main__':
    main()
