from unittest import TestCase, main
import bs4
from tested.another_bs_package import bs_page_getter
from tested.another_bs_package.bs_page_getter import get_page
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(bs_page_getter))
    return tests


class MyTest(TestCase):
    def test_is_get_page_bs_element_tag(self):
        self.assertIsInstance(get_page(url='https://fishki.net/1319528-evrejskie-anekdoty.html'), bs4.element.Tag)

    def test_is_there_alpha(self):
        self.assertTrue(
            (any(
                isinstance(i, str) for i in get_page(url='https://fishki.net/1319528-evrejskie-anekdoty.html')))
            is True,
            'нет букв')

    def test_page_get_func_is_wrong(self):
        with self.assertRaises(TypeError) as e:
            get_page(url='')
        self.assertEqual('Передан неверный тип данных, или -пустая строка', e.exception.args[0])


if __name__ == '__main__':
    main()
