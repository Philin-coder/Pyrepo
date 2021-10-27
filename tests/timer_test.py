from unittest import TestCase, main
from tested.m_timer_package import timer_mod
from tested.m_timer_package.timer_mod import t_clock_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(timer_mod))
    return tests


class MyTimerTest(TestCase):
    def test_works(self):
        self.assertEqual(t_clock_func(time_s=3682), ('часов 1', 'минут1', 'секунд22 '))

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            t_clock_func(time_s='3682')
        self.assertEqual('Ведите целое, положительное число ', e.exception.args[0])


if __name__ == '__main__':
    main()
