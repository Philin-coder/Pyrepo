from unittest import TestCase, main
from tested.re_world_counter_pacage import world_counter
from tested.re_world_counter_pacage.world_counter import wordcount
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(world_counter))
    return tests


class WorlCounterTest(TestCase):
    def test_wc_working(self):
        self.assertEqual(wordcount(text_str='проба первая'), 2)

    def test_wc_count_with_digs(self):
        self.assertEqual(wordcount(text_str='проба вторая 1112'), 3)

    def test_wc_digs_in_input(self):
        with self.assertRaises(TypeError) as e:
            wordcount(text_str=1112)
        self.assertEqual('Введите строку, через пробел', e.exception.args[0])


if __name__ == '__main__':
    main()
