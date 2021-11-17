from unittest import TestCase, main
from tested.glob_package import glober
from tested.glob_package.glober import user_name
from tested.glob_package.glober import global_name
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(glober))
    return tests


class MyGlobTest(TestCase):
    def test_user_name(self):
        self.assertEqual(user_name(text_string='jack'), ('hello,jack', 'But global name is,Bob'))

    def test_user_name_wrong(self):
        with self.assertRaises(TypeError) as e:
            user_name(text_string={'jack'})
        self.assertEqual(user_name(text_string='jack'), ('hello,jack', 'But global name is,Bob'))

    def test_global_name_right(self):
        self.assertEqual(global_name(), 'my global name=Bob')


if __name__ == '__main__':
    main()
