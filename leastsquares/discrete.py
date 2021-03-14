import functools

import numpy as np
import numpy.linalg as linalg


def regression(X, Y, Phi):
    def dot(f, g, X):
        return sum(f(x) * g(x) for x in X)

    n = len(Phi)

    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = dot(Phi[i], Phi[j], X)
    print("A:")
    print(A, "\n")

    B = np.zeros((n, 1))
    for i in range(n):
        f = {x: y for x, y in zip(X, Y)}
        B[i, 0] = dot(Phi[i], lambda x: f[x], X)
    print("B:")
    print(B, "\n")

    coeff = linalg.solve(A, B)
    print("Coefficients:")
    print(coeff)

    return coeff


def polynomial_regression(X, Y, degree):
    Phi = [functools.partial(lambda n, x: x**n, n) for n in range(degree + 1)]
    return regression(X, Y, Phi)


regression(
    [0, 1, 2, 3, 4, 5],
    [10, 11, 14, 19, 26, 35],
    [lambda _: 1, lambda x: x, lambda x: x**2],
)
