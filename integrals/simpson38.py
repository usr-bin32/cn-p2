import math


def integral(f, a, b):
    h = (b - a) / 3
    return (3 * h / 8) * (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(b))


def repeated_integral(f, a, b, m):
    def c(i):
        if i == 0 or i == m:
            return 1
        elif i % 3 == 0:
            return 2
        else:
            return 3

    if m % 3 != 0:
        raise Exception("`m` should be a multiple of 3.")

    h = (b - a) / m
    X = [a + h * i for i in range(m + 1)]

    return (3 * h / 8) * sum(c(i) * f(x) for i, x in enumerate(X))


def error_bound(M4, a, b, m):
    return M4 * (b - a)**5 / (180 * m**4)
