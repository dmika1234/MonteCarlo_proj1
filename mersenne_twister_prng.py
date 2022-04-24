import numpy as np
import time

def mersenne_twister_prng(n):
    s = int(time.time())
    rng_mt19937 = np.random.default_rng(np.random.MT19937(seed=s))
    numbers_mt19937 = rng_mt19937.random(n)
    return numbers_mt19937
