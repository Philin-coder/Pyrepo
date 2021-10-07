from unittest import TestCase, main
from tested.Polyb_crypt_decript_package import crypt_mod
from tested.Polyb_crypt_decript_package.crypt_mod import pol_crypt
from tested.Polyb_crypt_decript_package.crypt_mod import pol_decrypt
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(crypt_mod))
    return tests


class PolyTest(TestCase):
    def test_crypt_char_input(self):
        self.assertEqual(pol_crypt(text='hello world'), '22 15 26 26 33 45 33 36 26 14 ')

    def test_crypt_char_input(self):
        with self.assertRaises(TypeError) as e:
            pol_crypt(text=1)
        self.assertEqual('передана не строка', e.exception.args[0])

    def test_decrypt_char_input(self):
        self.assertEqual(pol_decrypt(crypt=pol_crypt(text='hello world')), 'helloworld')

    def test_decrypt_wrong_table(self):
        self.assertFalse((isinstance({'one', 'two', 'three'}, dict)) != False, 'Передан не словарь ')


if __name__ == '__main__':
    main()
