import numpy as np
from scipy.stats import norm


def monobit_test(sequence: np.ndarray, modulus: int) -> float:
    n = len(sequence)
    sn = 0
    nr_digits = int(np.log2(modulus))

    for nr in sequence:
        nr_binary_text = np.binary_repr(nr, nr_digits)
        vec_min1_plus1 = 2 * np.array(list(map(int, list(nr_binary_text)))) - 1
        sn = sn + np.sum(vec_min1_plus1)

    n_final = int(nr_digits * n)
    sn_final = sn / np.sqrt(n_final)
    normal01 = norm()
    p_value = 2 * (1 - normal01.cdf(np.abs(sn_final)))

    return p_value
