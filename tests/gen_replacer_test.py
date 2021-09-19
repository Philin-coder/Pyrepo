from unittest import TestCase, main
from tested.gen_replacer_package import gen_replaceer
from tested.gen_replacer_package.gen_replaceer import replacer_func
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(gen_replaceer))
    return tests


class ReplacerTest(TestCase):
    def test_it_works(self):
        self.assertEqual(replacer_func(comp='По результатам собеседования в КОМПАНИЯ были приняты следующие сотрудники',
                                       names=['Mars', 'Nike', 'Apple', 'Google']),
                         ['По результатам собеседования в Mars были приняты следующие сотрудники',
                          'По результатам собеседования в Nike были приняты следующие сотрудники',
                          'По результатам собеседования в Apple были приняты следующие сотрудники',
                          'По результатам собеседования в Google были приняты следующие сотрудники'])

    def test_tuple_in_input(self):
        with self.assertRaises(TypeError) as e:
            replacer_func(comp={'Попринятыследующиесотрудники '}, names=['Mars', 'Nike', 'Apple', 'Google'])
        self.assertEqual('Передан невернвйй тип даннных', e.exception.args[0])

    def test_set_in_input(self):
        with self.assertRaises(TypeError) as e:
            replacer_func(comp='Попринятыследующиесотрудники ', names={'Mars', 'Nike', 'Apple', 'Google'})
        self.assertEqual('Передан невернвйй тип даннных', e.exception.args[0])


if __name__ == '__main__':
    main()
