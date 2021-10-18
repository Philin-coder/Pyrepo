from unittest import TestCase, main
from tested.how_much_package import hm_paxk
from tested.how_much_package.hm_paxk import word_counter
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(hm_paxk))
    return tests


class HmTest(TestCase):
    def test_works(self):
        self.assertEqual(word_counter(w_let='мир', rep_pvt=2), ('итого', 9))

    def test_wrong_input_w_let(self):
        with self.assertRaises(TypeError) as e:
            word_counter(w_let=1, rep_pvt=5)
        self.assertEqual('передан неверный тип данных', e.exception.args[0])

    def test_wrong_input_r_rep(self):
        with self.assertRaises(TypeError) as e:
            word_counter(w_let='проба', rep_pvt=-5)
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
