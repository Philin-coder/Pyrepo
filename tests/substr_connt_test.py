from unittest import TestCase, main
from tested.substr_connt_package import substr_count
from tested.substr_connt_package.substr_count import inp_counter_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(substr_count))
    return tests


class SubstrConntTest(TestCase):
    def test_it_works(self):
        self.assertEqual(inp_counter_func(text_string='проба проба проба', text_substr='проба' ),3)
    def test_something(self):
        with self.assertRaises(TypeError) as e:
            inp_counter_func(text_string=123, text_substr=1 ),
        self.assertEqual('Введите непустую строку',e.exception.args[0])


if __name__ == '__main__':
    main()
