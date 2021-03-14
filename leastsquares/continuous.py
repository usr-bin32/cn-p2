import functools

import numpy as np
import numpy.linalg as linalg
import scipy.integrate as integrate


def regression(f, a, b, Phi):
    def dot(f, g, a, b):
        value, _ = integrate.quad(lambda x: f(x) * g(x), a, b)
        return value

    n = len(Phi)

    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = dot(Phi[i], Phi[j], a, b)
    print("A:")
    print(A, "\n")

    B = np.zeros((n, 1))
    for i in range(n):
        B[i, 0] = dot(Phi[i], f, a, b)
    print("B:")
    print(B, "\n")

    coeff = linalg.solve(A, B)
    print("Coefficients:")
    print(coeff)

    return coeff


def polynomial_regression(f, a, b, degree):
    Phi = [functools.partial(lambda n, x: x**n, n) for n in range(degree + 1)]
    return regression(f, a, b, Phi)


regression(
    lambda x: 1 / (x + 2),
    -1, 1,
    [lambda _: 1, lambda x: x, lambda x: x**2],
)
