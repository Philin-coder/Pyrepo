from unittest import TestCase, main
from tested.inaudible_package import ina
from tested.inaudible_package.ina import inaudible
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(ina))
    return tests


class InaudibleTestCase(TestCase):
    def test_works(self):
        self.assertEqual(
            inaudible(
                text='Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно '
                     'небольшой тренировки - и вы сможете это делать.'),
            'двтльнй фкт н ткст н зк НРЗБРЧВ кзвтс двльн прст чтть Дсттчн нбльшй трнрвк в смжт т длть')

    # def test_int_in_input(self):
    #     with self.assertRaises(TypeError) as e:
    #         inaudible(text=1)
    #     self.assertEqual('Введена не строка', e.exception.args[0])


if __name__ == '__main__':
    main()
