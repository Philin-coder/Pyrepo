from unittest import TestCase, main
from tested.setcontroller_package import setcontrolle
from tested.setcontroller_package.setcontrolle import nabor


class SetControllerTest(TestCase):

    def test_char_in_input(self):
        with self.assertRaises(TypeError) as e:
            nabor(k='-')
        self.assertEqual('Введите целое чисдл для количества наборов и набор  из целых  числе', e.exception.args[0])


if __name__ == '__main__':
    main()
