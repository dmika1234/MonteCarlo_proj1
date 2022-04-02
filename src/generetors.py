import numpy as np


class LCG:
    def __init__(self, modulus, a, c):
        self.modulus = modulus
        self.a = a
        self.c = c

    def generate_numbers(self, n: int, seed: float) -> np.ndarray:
        res = np.zeros(n, dtype='int')
        res[0] = seed % self.modulus
        for i in np.arange(1, n):
            res[i] = (self.a * res[i - 1] + self.c) % self.modulus
        return res


class GLCG:
    def __init__(self, modulus, *args):
        self.modulus = modulus
        self.coefficients = np.array(args)
        self.k = len(args)

    def generate_numbers(self, n: int, seeds: list) -> np.ndarray:
        seeds = np.array(seeds)
        res = np.zeros(n, dtype='int')
        res[0:self.k] = np.mod(seeds, self.modulus)
        for i in np.arange(self.k, n):
            res[i] = np.mod(np.sum(self.coefficients * res[(i-self.k):i]), self.modulus)
        return res


