from unittest import TestCase, main
from tested.summ_devs_package import summdevs
from tested.summ_devs_package.summdevs import summ_of_devs
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(summdevs))
    return tests


class SummdevsTest(TestCase):
    def test_int_in_input(self):
        self.assertEqual(summ_of_devs(x=128), 255)

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            summ_of_devs(x='128')
        self.assertEqual('Введите целое число', e.exception.args[0])


if __name__ == '__main__':
    main()
