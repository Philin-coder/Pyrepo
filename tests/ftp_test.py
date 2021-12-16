from unittest import TestCase, main
from tested.ftp_pack import ftp_loader
from tested.ftp_pack.ftp_loader import ftp_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(ftp_loader))
    return tests


class FtpTest(TestCase):
    def test_page_get_func_wrong(self):
        with self.assertRaises(TypeError) as e:
            ftp_func(host='', user='', pass_w='', filename='')
        self.assertEqual('передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
