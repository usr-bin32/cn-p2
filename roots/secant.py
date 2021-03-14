import math

import numpy as np
import pandas as pd


class Newton:
    def __init__(self, f, x0, x1):
        self.f = f
        self.x0 = x0
        self.x1 = x1

        self.history = {
            "x0": [],
            "x1": [],
            "x2 = φ(x)": [],
            "RErr": [],
            "AErr": [],
        }

    def next(self):
        f_x0 = self.f(self.x0)
        f_x1 = self.f(self.x1)
        denom = (f_x1 - f_x0)

        if denom == 0:
            return

        x2 = self.x1 - f_x1 * (self.x1 - self.x0) / denom

        self.history["x0"].append(self.x0)
        self.history["x1"].append(self.x1)
        self.history["x2 = φ(x)"].append(x2)
        self.history["RErr"].append(abs((x2 - self.x1) / x2))
        self.history["AErr"].append(abs(x2 - self.x1))

        self.x0 = self.x1
        self.x1 = x2

    def print(self):
        print(pd.DataFrame(self.history))


it = Newton(lambda x: x**(1/2) - 5 * math.e**(-x), 1.4, 1.5)
for _ in range(10):
    it.next()
it.print()
