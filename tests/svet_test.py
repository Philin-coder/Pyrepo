from unittest import TestCase, main
from tested.svetofor_psckage import svet
from tested.svetofor_psckage.svet import example
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(svet))
    return tests


class SvetTest(TestCase):
    def test_Pass(self):
        self.assertEqual(example(30, 20, 145, 5, 3), 'Pass')

    def test_work(self):
        self.assertEqual(example(10, 70, 200, 20, 4), '50.000 67.500')


if __name__ == '__main__':
    main()
