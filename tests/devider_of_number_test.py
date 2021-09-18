from unittest import TestCase, main
from tested.ammount_of_deviders_packaage import deviders
from tested.ammount_of_deviders_packaage.deviders import num_devs
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(deviders))
    return tests


class num_dev_tests(TestCase):
    def test_ints_in_input(self):
        self.assertEqual(num_devs(12), 6)

    def test_chars_in_input(self):
        with self.assertRaises(TypeError) as e:
            num_devs('12')
        self.assertEqual('Введите целое число', e.exception.args[0])

    def test_dicts_in_input(self):
        with self.assertRaises(TypeError) as e:
            num_devs({1: 1})
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
