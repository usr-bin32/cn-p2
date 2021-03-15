import math


def integral(f, a, b):
    h = b - a
    return h * f(a)


def repeated_integral(f, a, b, m):
    h = (b - a) / m
    X = [a + h * i for i in range(m + 1)]

    return h * sum(f(x) for x in X)


def error_bound(M1, a, b, m):
    return M1 * (b - a)**2 / (2 * m)
