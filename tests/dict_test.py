from unittest import TestCase, main
from tested.dict_package import dictor
from tested.dict_package.dictor import dict_gen
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dictor))
    return tests


class DcitTestCase(TestCase):
    def test_is_dict(self):
        self.assertEqual(dict_gen(list_key=["frog", "snail", "bird"], list_value=[1, 2, 3]),
                         {'frog': 1, 'snail': 2, 'bird': 3})

    def test_is_dict_inp(self):
        self.assertEqual(dict_gen(list_key=["Капитан", "Майор", "Полковтк"], list_value=[5, 6, 9]),
                         {'Капитан': 5, 'Майор': 6, 'Полковтк': 9})

    def test_is_dict_true(self):
        self.assertIsInstance({'Капитан': 5, 'Майор': 6, 'Полковтк': 9}, dict)

    def test_is_dict_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            dict_gen(list_key=["Капитан", "Майор", "Полковтк"], list_value={5, 6, 9})
            self.assertEqual('e', e.exception.args[0])

        if __name__ == '__main__':
            main()
