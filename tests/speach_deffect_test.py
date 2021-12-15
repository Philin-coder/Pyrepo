from unittest import TestCase, main
from tested.speach_defffect_package import sd
from tested.speach_defffect_package.sd import speach_defect
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(sd))
    return tests


class SDTest(TestCase):
    def test_speach_def_right(self):
        self.assertEqual(speach_defect(text="""\
    Привет
    Не могу до тебя дозвониться
    Не могу до тебя дозвониться
    Не могу до тебя дозвониться
    Когда доедешь до дома
    Ага, жду
    Ага, жду"""), ['    Не могу до тебя дозвониться', '    Когда доедешь до дома', '    Ага, жду'])

    def test_speach_def_wrong(self):
        with self.assertRaises(TypeError) as e:
            speach_defect(text=123)
        self.assertEqual('Передан неверный тип данных', e.exception.args[0])


if __name__ == '__main__':
    main()
