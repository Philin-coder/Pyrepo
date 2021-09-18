from unittest import TestCase, main
from tested.pin_code_package import pin_mod
from tested.pin_code_package.pin_mod import is_valid_pin

import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(pin_mod))
    return tests


class PInTest(TestCase):
    def test_validator_true(self):
        with self.subTest(is_valid_pin(pin='7-101-4')):
            self.assertEqual(is_valid_pin(pin='7-101-4'), True)


    def test_validator_false(self):
        with self.subTest(is_valid_pin(pin='12-22-16')):
            self.assertEqual(is_valid_pin(pin='12-22-16'), False)


if __name__ == '__main__':
    main()
