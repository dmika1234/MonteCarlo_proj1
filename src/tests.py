import numpy as np
from scipy.stats import norm, chisquare, kstest
from scipy.special import erfc
from other_functions import *
from generetors import *


def monobit_test(sequence, modulus: int) -> float:
    """
    :param sequence: sequence of BITS
    :param modulus: maximal possible number - 1 (ex. 2^32)
    :return: p_value of test
    """
    n = len(sequence)
    nr_digits = int(np.log2(modulus))
    bit_str = ''.join(sequence)
    vec_min1_plus1 = 2 * np.array(list(map(int, list(bit_str)))) - 1
    sn = np.sum(vec_min1_plus1)
    n_final = int(nr_digits * n)
    sn_final = sn / np.sqrt(n_final)
    normal01 = norm()
    p_value = 2 * (1 - normal01.cdf(np.abs(sn_final)))

    return p_value


def runs_test(sequence): #zakladam ze na wejsciu dostajemy ciag zerojedynkowy
    sequence = str(sequence)
    n = len(sequence)
    t = 2/n #tau statistic nie wiem czy sqrt(n) czy n (raz jest tak a raz inaczej w skrypcie)
    t = 2 / np.sqrt(n) # W pliku NIST był sqrt(n)
    pi = 0
    V = 1
    for i in range(n):
        pi = pi + int(sequence[i])
        if i < n-1:
            if sequence[i] != sequence[i+1]:
                V = V + 1
    pi = pi/n
    p_value = erfc((V-2*n*pi*(1-pi))/(2*np.sqrt(2*n)*pi*(1-pi)))
    if abs(pi - 1/2) < t:
        return "the test is not run"
    else:
        return p_value


def chi_square_test(f_obs, f_exp=None, ddof=0, axis=0): #zakladam ze na wejsciu dostajemy ciag zerojedynkowy
    f_obs = str(f_obs)
    working_lst = []
    for i in range(len(f_obs)):
        working_lst.append(int(f_obs[i]))
    f_obs = working_lst
    return chisquare(f_obs, f_exp, ddof, axis)[1] #p_value




