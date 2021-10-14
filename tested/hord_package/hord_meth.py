from typing import Callable


def secant(f: Callable[[float], float], x0: float, eps: float = 1e-7, k_max: int = 1e3) -> float:
    """
    solves f(x) = 0 by secant method with precision eps
    :param f: f
    :param x0: starting point
    :param eps: precision wanted
    :param k_max: maximum number
    :return: root of f(x) = 0

    """
    x, x_prev, i = x0, x0 + 2 * eps, 0

    while abs(x - x_prev) >= eps and i < k_max:
        x, x_prev, i = x - f(x) / (f(x) - f(x_prev)) * (x - x_prev), x, i + 1

    return x
