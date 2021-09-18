from unittest import TestCase, main
from tested.eval_demo_pacage import eval_demo
from tested.eval_demo_pacage.eval_demo import eval_demo_func
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(eval_demo))
    return tests


class EvalDemoTest(TestCase):
    def test_eval_int_in_input_works(self):
        self.assertEqual(eval_demo_func(x=12), 248832)

    def test_eval_char_in_input(self):
        with self.assertRaises(TypeError)as e:
            eval_demo_func(x='12')
        self.assertEqual('введите число',e.exception.args[0])


if __name__ == '__main__':
    main()
