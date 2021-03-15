import math


def integral(f, a, b):
    h = (b - a) / 2
    return (h / 3) * (f(a) + 4 * f(a + h) + f(b))


def repeated_integral(f, a, b, m):
    def c(i):
        if i == 0 or i == m:
            return 1
        elif i % 2 == 0:
            return 2
        else:
            return 4

    if m % 2 != 0:
        raise Exception("`m` should be a multiple of 2.")

    h = (b - a) / m
    X = [a + h * i for i in range(m + 1)]

    return (h / 3) * sum(c(i) * f(x) for i, x in enumerate(X))


def error_bound(M4, a, b, m):
    return M4 * (b - a)**5 / (80 * m**4)
