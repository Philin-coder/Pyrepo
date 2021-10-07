from unittest import TestCase, main
from tested.cezar_package import cezar_crypt
from tested.cezar_package.cezar_crypt import cezar_crypto
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(cezar_crypt))
    return tests


class CezarTest(TestCase):
    def test_cezar_crypt_works_key2(self):
        self.assertEqual(cezar_crypto(step=2, text_str='проба'), 'Result: "стргв"')

    def test_cezar_crypt_works_key3(self):
        self.assertEqual(cezar_crypto(step=3, text_str='война'), 'Result: "есмрг"')

    def test_cezar_crypt_works_key2_str(self):
        self.assertEqual(cezar_crypto(step=2, text_str='идущие на смерть приветствуют тебя'),
                         'Result: "кёхыкжбпвбуожтфюбсткджфуфдхафбфжгб"')

    def test_cezar_crypt_works_key_int(self):
        with self.assertRaises(TypeError) as e:
            cezar_crypto(step=2, text_str=2)
        self.assertEqual('Введите ключ(целое, положительное  число) и шифруемую строку маленькими буквами',
                         e.exception.args[0])


if __name__ == '__main__':
    main()
