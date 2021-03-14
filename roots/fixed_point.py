import math

import numpy as np
import pandas as pd


class FixedPoint:
    def __init__(self, phi, x0):
        self.phi = phi
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


it = FixedPoint(lambda x: 1 + 2 / x, 2.5)
for _ in range(10):
    it.next()
it.print()
