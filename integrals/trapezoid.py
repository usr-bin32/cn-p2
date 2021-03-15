import math


def integral(f, a, b):
    h = b - a
    return (h / 2) * (f(a) + f(b))


def repeated_integral(f, a, b, m):
    def c(i):
        if i == 0 or i == m:
            return 1
        else:
            return 2

    h = (b - a) / m
    X = [a + h * i for i in range(m + 1)]

    return (h / 2) * sum(c(i) * f(x) for i, x in enumerate(X))


def error_bound(M2, a, b, m):
    return M2 * (b - a)**3 / (12 * m**2)
