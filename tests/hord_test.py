from unittest import TestCase, main
from tested.hord_package.hord_meth import secant
from math import sin


class TestSecant(TestCase):
    def test_0(self):
        def f(x: float) -> float:
            return x ** 2 - 20 * sin(x)

        x0, x_star = 2, 2.7529466338187049383

        self.assertAlmostEqual(secant(f, x0), x_star)


if __name__ == '__main__':
    main()
