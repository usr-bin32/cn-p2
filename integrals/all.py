import math

import pandas as pd

import midpoint
import rectangle
import trapezoid
import simpson38
import simpson13


def integral(f, a, b, exact=None):
    I_rectangle = rectangle.integral(f, a, b)
    I_midpoint = midpoint.integral(f, a, b)
    I_trapezoid = trapezoid.integral(f, a, b)
    I_simpson13 = simpson13.integral(f, a, b)
    I_simpson38 = simpson38.integral(f, a, b)

    data = {}

    data["Name"] = [
        "Rectangle",
        "Midpoint",
        "Trapezoid",
        "Simpson 1/3",
        "Simpson 3/8",
    ]
    data["I"] = [
        I_rectangle,
        I_midpoint,
        I_trapezoid,
        I_simpson13,
        I_simpson38,
    ]
    if exact is not None:
        data["AErr"] = [
            abs(I_rectangle - exact),
            abs(I_midpoint - exact),
            abs(I_trapezoid - exact),
            abs(I_simpson13 - exact),
            abs(I_simpson38 - exact),
        ]
        data["RErr"] = [
            abs(I_rectangle - exact / exact),
            abs(I_midpoint - exact / exact),
            abs(I_trapezoid - exact / exact),
            abs(I_simpson13 - exact / exact),
            abs(I_simpson38 - exact / exact),
        ]

    print(pd.DataFrame(data), "\n")


def repeated_integral(f, a, b, m, exact=None):
    I_rectangle = rectangle.repeated_integral(f, a, b, m)
    I_midpoint = midpoint.repeated_integral(f, a, b, m)
    I_trapezoid = trapezoid.repeated_integral(f, a, b, m)
    I_simpson13 = simpson13.repeated_integral(f, a, b, m)
    I_simpson38 = simpson38.repeated_integral(f, a, b, m)

    data = {}

    data["Name"] = [
        "Rectangle",
        "Midpoint",
        "Trapezoid",
        "Simpson 1/3",
        "Simpson 3/8",
    ]
    data["I"] = [
        I_rectangle,
        I_midpoint,
        I_trapezoid,
        I_simpson13,
        I_simpson38,
    ]
    if exact is not None:
        data["AErr"] = [
            abs(I_rectangle - exact),
            abs(I_midpoint - exact),
            abs(I_trapezoid - exact),
            abs(I_simpson13 - exact),
            abs(I_simpson38 - exact),
        ]
        data["RErr"] = [
            abs(I_rectangle - exact / exact),
            abs(I_midpoint - exact / exact),
            abs(I_trapezoid - exact / exact),
            abs(I_simpson13 - exact / exact),
            abs(I_simpson38 - exact / exact),
        ]

    print(pd.DataFrame(data), "\n")

integral(lambda x: 1 / x, 1, 4, exact=math.log(4))
repeated_integral(lambda x: 1 / x, 1, 4, 120, exact=math.log(4))
