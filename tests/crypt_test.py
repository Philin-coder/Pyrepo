from unittest import TestCase, main
from tested.crypto_package import crypter
from tested.crypto_package.crypter import crypto
from tested.crypto_package.crypter import encrypt
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(crypter))
    return tests


class CryptTest(TestCase):
    def test_crypto_right(self):
        self.assertEqual(crypto(string_to_crypt='Скажи мне, кто твой друг и я скажу тебе, кто ты', key=5),
                         ',вукукстж нгкы мйеСтаое тяаи  о ите дбтрож  , к')

    def test_encrypt_right(self):
        self.assertEqual(
            encrypt(string_to_encrypt=crypto(string_to_crypt='Скажи мне, кто твой друг и я скажу тебе, кто ты', key=5),
                    key=5), 'Скажи мне, кто твой друг и я скажу тебе, кто ты')

    def test_is_crypt_string(self):
        self.assertIsInstance(crypto(string_to_crypt='Пример шифруемой строки\nметодом перестановки', key=5), str)

    def test_char_only(self):
        with self.assertRaises(TypeError) as e:
            crypto(string_to_crypt='Пример шифруе1мой строки\nметодом перестановки', key=5)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_not_ints(self):
        with self.assertRaises(TypeError) as e:
            crypto(string_to_crypt=123, key=5)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_not_key_as_char(self):
        with self.assertRaises(TypeError) as e:
            crypto(string_to_crypt='Пример шифруемой строки\nметодом перестановки', key='5')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_not_empty_str(self):
        with self.assertRaises(TypeError) as e:
            crypto(string_to_crypt='', key=5)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_encrypt_is_not_none(self):
        with self.assertRaises(TypeError) as e:
            encrypt(string_to_encrypt=None, key=5)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_encrypt_is_not_key_char(self):
        with self.assertRaises(TypeError) as e:
            encrypt(string_to_encrypt=crypto(string_to_crypt='Пример шифруемой строки\nметодом перестановки', key=5),
                    key='5')
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_crypt_key_is_not_none(self):
        with self.assertRaises(TypeError) as e:
            crypto(string_to_crypt='Пример шифруемой строки\nметодом перестановки', key=None)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_encrypt_key_is_not_none(self):
        with self.assertRaises(TypeError) as e:
            encrypt(string_to_encrypt=crypto(string_to_crypt='Пример шифруемой строки\nметодом перестановки', key=5),
                    key=None)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
