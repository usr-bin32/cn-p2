import math


def integral(f, a, b):
    h = b - a
    return h * f((a + b) / 2)


def repeated_integral(f, a, b, m):
    h = (b - a) / m
    X = [a + h * i for i in range(m + 1)]

    return h * sum(f((x1 + x2) / 2) for x1, x2 in zip(X, X[1:]))


def error_bound(M2, a, b, m):
    return M2 * (b - a)**3 / (24 * m**2)
