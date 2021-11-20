from unittest import TestCase, main
from tested.gert_uniq_tags_package import tag_gettet
from tested.gert_uniq_tags_package.tag_gettet import get_html
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(tag_gettet))
    return tests


class ParseTest(TestCase):
    def test_is_get_html_set(self):
        self.assertEqual(get_html(url='http://htmlbook.ru/samhtml5/ustarevshie-tegi-i-atributy/'),
                         {'isindex', 'option', 'rb', 'big', 'ruby', 'basefont', 'blink', 'iframe', 'multicol', 'video',
                          'img', 'embed', 'xmp', 'ul', 'dir', 'html', 'form', 'frame', 'marquee', 'font', 'body', 'br',
                          'object', 'meta', 'del', 'input', 'head', 'frameset', 'bgsound'})

    def test_what_is_get_html_set(self):
        self.assertIsInstance(get_html(url='http://htmlbook.ru/samhtml5/ustarevshie-tegi-i-atributy/'), set)

    def test_is_get_html_alpha(self):
        self.assertTrue(
            (any(isinstance(i, str) for i in
                 get_html(url='http://htmlbook.ru/samhtml5/ustarevshie-tegi-i-atributy/'))) is True,
            'не буквы')

    def test_is_not_None(self):
        self.assertIsNotNone(get_html(url='http://htmlbook.ru/samhtml5/ustarevshie-tegi-i-atributy/'))

    def test_get_html_wrong(self):
        with self.assertRaises(TypeError) as e:
            get_html(url='')
        self.assertEqual('Передан неправильный тип данных, либо - пустая строка', e.exception.args[0])


if __name__ == '__main__':
    main()
