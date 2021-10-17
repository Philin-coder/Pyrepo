from unittest import TestCase, main
from tested.late_package import later
from tested.late_package.later import late
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(later))
    return tests


class LateTest(TestCase):
    def test_twenty_before(self):
        self.assertEqual(late('9:00', '10:00', [5, 15, 25]), 'Выйти через 20 минут')

    def test_late(self):
        self.assertEqual(late('9:20', '9:35', [4, 25, 30]), 'Опоздание')

    def test_no_late(self):
        self.assertEqual(late('12:00', '12:40', [0, 1, 4, 6, 25]), 'Выйти через 0 минут')

    def test_wrong_input_now(self):
        with self.assertRaises(TypeError) as e:
            late(12.00, '12:40', [0, 1, 4, 6, 25])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_wrong_input_deadline(self):
        with self.assertRaises(TypeError) as e:
            late('12:40', 12, [0, 1, 4, 6, 25])
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_wrong_input_bus(self):
        with self.assertRaises(TypeError) as e:
            late('12:40', '12:40', {0, 1, 4, 6, 25})
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
