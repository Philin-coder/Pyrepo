from unittest import TestCase, main
from tested.arifm_package import sim_arifm
from tested.arifm_package.sim_arifm import perv
from tested.arifm_package.sim_arifm import suber
import doctest



def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sim_arifm))
    return tests


class SimArTest(TestCase):
    def test_perv_is_float(self):
        self.assertIsInstance(perv(a=12), float)

    def test_suber_is_str(self):
        self.assertIsInstance(suber(x=perv(a=12), y=perv(a=1)), str)

    def test_prev_right(self):
        self.assertEqual(perv(a=12), 8.71673508601987)

    def test_suber_right(self):
        self.assertEqual(suber(x=perv(a=12), y=perv(a=1)), 'точное значение интеграла 8.44405944272629')

    def test_perv_wrong(self):
        with self.assertRaises(TypeError) as e:
            perv(a='12')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_suber_wrong(self):
        with self.assertRaises(TypeError) as e:
            suber(x=perv(a='12'), y=perv(a='1'))
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
