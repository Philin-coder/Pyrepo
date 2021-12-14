from unittest import TestCase, main
from tested.mc_loren_pack import mc_lor
from tested.mc_loren_pack.mc_lor import mck_loren
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mc_lor))
    return tests


class MckLorenTest(TestCase):
    def test_mck_loren_right(self):
        self.assertEqual(mck_loren(x=12.0, e=15.1, km=4), ('аналитически=', 81377.39571257407))

    def test_mck_loren_wrong(self):
        with self.assertRaises(TypeError) as e:
            mck_loren(x='12.0', e='15.1', km='4')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
