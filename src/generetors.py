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
            res[i] = np.mod(np.sum(self.coefficients * res[(i - self.k):i]), self.modulus)
        return res


class RC4:
    def __init__(self, m: int):
        self.m = m

    def KSA(self, key) -> np.ndarray:
        key = np.array(key)
        key_len = len(key)
        s = np.arange(0, self.m)
        j = 0
        for i in np.arange(self.m):
            j = (j + s[i] + key[i % key_len]) % self.m
            s[j], s[i] = s[i], s[j]  # swap values
        return s

    def PRGA(self, s: np.ndarray, n: int) -> np.ndarray:
        i = 0
        j = 0
        y = np.zeros(n)
        for r in np.arange(n):
            i = (i + 1) % self.m
            j = (j + s[i]) % self.m

            s[i], s[j] = s[j], s[i]  # swap values
            y[r] = s[(s[i] + s[j]) % self.m]
        return y

    def generate_numbers(self, n, key) -> np.ndarray:
        s = self.KSA(key)
        res = np.array(self.PRGA(s, n), dtype='int32')
        return res
