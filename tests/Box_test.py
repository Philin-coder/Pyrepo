from unittest import TestCase, main
from tested.box_package import boxer
from tested.box_package.boxer import box
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(boxer))
    return tests


class BoxTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(box(s=4), 0.7698003589195009)

    def test_chars_in_input(self):
        with self.assertRaises(TypeError) as e:
            box(s='12')
        self.assertEqual('должно быть введено целое число', e.exception.args[0])

    def test_empty_in_input(self):
        with self.assertRaises(TypeError) as e:
            box(s='')
        self.assertEqual('должно быть введено целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
