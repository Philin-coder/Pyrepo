from unittest import TestCase, main
from tested.page_text_get_package import pager
from tested.page_text_get_package.pager import page_get_func
import doctest
import bs4


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(pager))
    return tests


class GetWebPageTest(TestCase):
    def test_page_get_func_is_not_empty(self):
        self.assertIsNotNone(page_get_func(
            url='https://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python '))

    def test_page_get_func_is_bs(self):
        self.assertIsInstance(page_get_func(
            url='https://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python '),
            bs4.BeautifulSoup)

    def test_is_there_alpha(self):
        self.assertTrue((any(isinstance(i, str) for i in page_get_func(
            url='https://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python')))
                        is True,
                        'нет букв')

    def test_page_get_func_wrong(self):
        with self.assertRaises(TypeError) as e:
            page_get_func(url='')
        self.assertEqual('Передан неверный тип данных, или -пустая строка', e.exception.args[0])


if __name__ == '__main__':
    main()
