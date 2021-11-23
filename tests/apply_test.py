from unittest import TestCase, main
from tested.apply_package import applier
from tested.apply_package.applier import apply_example
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(applier))
    return tests


class AplTest(TestCase):
    def test_is_tuple(self):
        self.assertIsInstance(apply_example(*[1, 2, 3], **{'a': 4, 'b': 5}), tuple)

    def test_works(self):
        self.assertEqual(apply_example(*[1, 2, 3], **{'a': 4, 'b': 5}), (1, 2, 3, 4, 5))


if __name__ == '__main__':
    main()
