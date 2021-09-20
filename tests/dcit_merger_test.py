from unittest import TestCase, main
from tested.dict_merger_package import dict_merger
from tested.dict_merger_package.dict_merger import dict_mergers_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(dict_merger))
    return tests


class DictMergerTest(TestCase):
    def test_works(self): self.assertEqual(dict_mergers_func(
        names=[';;Люда', 'Тимафей;;', 'Петр;', ';;Яна', ';;Мефодий', ';Ксения;', 'Дамира'],
        surname=['Иванова', 'Джонс', 'Киселев', 'Солнцева', 'Петрова', 'Смирнова', 'Алексеева'],
        ags=[8, 34, 17, 2, 86, 32, 101]),
        {'Люда Иванова': 8, 'Тимафей Джонс': 34, 'Петр Киселев': 17, 'Яна Солнцева': 2, 'Мефодий Петрова': 86,
         'Ксения Смирнова': 32, 'Дамира Алексеева': 101})

    def test_wrong_input_first(self):
        with self.assertRaises(TypeError) as e:
            dict_mergers_func(names=[2, ';;Люда', 'Тимафей;;', 'Петр;', ';;Яна', ';;Мефодий', ';Ксения;', 'Дамира'],
                              surname=['Иванова', 'Джонс', 'Киселев', 'Солнцева', 'Петрова', 'Смирнова', 'Алексеева'],
                              ags=[8, 34, 17, 2, 86, 32, 101])
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_wrong_input_second(self):
        with self.assertRaises(TypeError) as e:
            dict_mergers_func(names=[';;Люда', 'Тимафей;;', 'Петр;', ';;Яна', ';;Мефодий', ';Ксения;', 'Дамира'],
                              surname=[1, 'Иванова', 'Джонс', 'Киселев', 'Солнцева', 'Петрова', 'Смирнова',
                                       'Алексеева'],
                              ags=[8, 34, 17, 2, 86, 32, 101])
            self.assertEqual('Передан неверный тип данных', e.exception.args[0])

    def test_wrong_input_third(self):
        with self.assertRaises(TypeError) as e:
            dict_mergers_func(names=[';;Люда', 'Тимафей;;', 'Петр;', ';;Яна', ';;Мефодий', ';Ксения;', 'Дамира'],
                              surname=['Иванова', 'Джонс', 'Киселев', 'Солнцева', 'Петрова', 'Смирнова', 'Алексеева'],
                              ags=['a', 8, 34, 17, 2, 86, 32, 101])
            self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
