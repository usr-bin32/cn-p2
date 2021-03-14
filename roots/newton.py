import math

import numpy as np
import pandas as pd


class Newton:
    def __init__(self, f, df, x0):
        self.phi = lambda x: x - f(x) / df(x)
        self.x = x0

        self.history = {
            "x": [],
            "φ(x)": [],
            "RErr": [],
            "AErr": [],
        }

    def next(self):
        phi_x = self.phi(self.x)

        self.history["x"].append(self.x)
        self.history["φ(x)"].append(phi_x)
        self.history["RErr"].append(abs((phi_x - self.x) / phi_x))
        self.history["AErr"].append(abs(phi_x - self.x))

        self.x = phi_x

    def print(self):
        print(pd.DataFrame(self.history))


it = Newton(lambda x: x + np.log(x), lambda x: 1 + 1/x, 1)
for _ in range(25):
    it.next()
it.print()
