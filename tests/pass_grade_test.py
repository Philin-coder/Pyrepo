from unittest import TestCase, main
from tested.pass_grade_package import pass_grade
from tested.pass_grade_package.pass_grade import pass_gradient
import doctest
import random
import re
import string


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(pass_grade))
    return tests


class PassGradeTest(TestCase):
    def test_is_random_int(self):
        self.assertTrue((1 <= random.randint(1, 10) <= 10) is True, 'не рандом')

    def test_num_test(self):
        self.assertTrue((all(isinstance(i, int) for i in list(
            map(int, re.findall(r'\d+',
                                f'{str([random.randint(1, 10) for _ in range(5)])}'.removeprefix(
                                    '[').removesuffix(']').strip()))))) is True, 'не первая степень  ')

    def test_alpha_test(self):
        sep = ''
        fnd = sep.join([
            f'{str([random.randint(1, 10) for _ in range(5)])}'.removeprefix('[').removesuffix(']').strip(),
            f'{sep.join(random.choice(string.ascii_letters) for _ in range(5))}'])
        self.assertTrue((any(isinstance(i, int) for i in list(map(int, re.findall(r'\d+', fnd)))) and (
            any(i.isalpha() for i in re.findall(r'[^0-9,\s]', fnd)))
                         ) is True, 'не вторая степень')

    def test_last(self):
        sp = ''
        f = sp.join([
            f'{str([random.randint(1, 10) for _ in range(5)])}'.removeprefix('[').removesuffix(']').strip(),
            f'{sp.join(random.choice(string.ascii_letters) for _ in range(5))}'
            f'{sp.join(random.choice(string.punctuation) for _ in range(5))}'
        ])

        self.assertTrue((any(isinstance(i, int) for i in list(map(int, re.findall(r'\d+', f)))) and any(
            i not in string.punctuation and not i.isspace() and not i.isdigit() for i in f) and any(
            i for i in re.findall(r'[^0-9,a-zA-Z\s]', f))) is True, 'не третья степень')

    def test_wrong_input(self):
        with self.assertRaises(TypeError) as e:
            pass_gradient(star_p='1', end_p='10', grade='4', n='3')
        self.assertEqual('Введите целые числа', e.exception.args[0])


if __name__ == '__main__':
    main()
