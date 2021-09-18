from unittest import TestCase, main
import doctest
from tested.deldigit_package import deldigit
from tested.deldigit_package.deldigit import del_digit_func


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(deldigit))
    return tests


class DelDigitTest(TestCase):
    def test_all_right(self):
        self.assertEqual(del_digit_func('123a'), 'a')

    def test_is_emp_string(self):
        with self.assertRaises(ValueError) as e:
            del_digit_func("")
        self.assertEqual('проверьте входные данные(строка не должна быть пустой', e.exception.args[0])


if __name__ == '__main__':
    main()
