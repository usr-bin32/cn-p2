import math

import numpy as np
import pandas as pd


class Bissection:
    def __init__(self, f, a, b):
        self.f = f
        self.a = a
        self.b = b

        self.x0 = a
        self.history = {
            "a": [],
            "b": [],
            "x": [],
            "f(a)": [],
            "f(b)": [],
            "f(x)": [],
            "RErr": [],
            "AErr": [],
        }

    def min_k(self, x_err):
        return math.ceil(np.log((self.b - self.a) / x_err) / np.log(2))

    def next(self):
        x = (self.a + self.b) / 2

        f_a = self.f(self.a)
        f_b = self.f(self.b)
        f_x = self.f(x)

        self.history["a"].append(self.a)
        self.history["b"].append(self.b)
        self.history["x"].append(x)
        self.history["f(a)"].append(f_a)
        self.history["f(b)"].append(f_b)
        self.history["f(x)"].append(f_x)
        self.history["RErr"].append(abs((x - self.x0) / x))
        self.history["AErr"].append(abs(x - self.x0))

        if f_a * f_x < 0:
            self.b = x
        else:
            self.a = x
        
        self.x0 = x

    def print(self):
        print(pd.DataFrame(self.history))


it = Bissection(lambda x: x**2 + np.log(x), 0.5, 1)
for _ in range(it.min_k(10**-2)):
    it.next()
it.print()
