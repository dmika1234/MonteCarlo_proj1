import numpy as np
from scipy.stats import norm, chisquare, kstest
from scipy.special import erfc, gammainc
from other_functions import *
from generetors import *


def compute_nrs_in_bins(partition, points: np.ndarray):
    bins = np.zeros(len(partition) - 1)

    for i in range(len(bins)):
        ffrom = partition[i]
        tto = partition[i + 1]
        bins[i] = ((points > ffrom) & (points <= tto)).sum()
    # bins_probs[i]=tto-ffrom

    return bins


def second_level_test(sequence: np.ndarray, s: int = 10):
    """
    :param sequence: Sequence of p_values(must be numpy array)
    :param s: Partition size
    :return: p_value of the test
    """
    R = len(sequence)
    partition = np.append((np.arange(s) / s), 1)
    bins = compute_nrs_in_bins(partition, sequence)
    # bins_exp = np.full(s, R / s)
    p_value = chisquare(bins)[1]
    return p_value


def monobit_test(sequence, modulus: int = 2) -> float:
    """
    :param sequence: sequence of BITS: ['10', '01', '11']
    :param modulus: maximal possible number - 1 (ex. 2^32)
    :return: p_value of test
    """
    sequence = list(map(str, sequence))
    if type(sequence) == str:
        bit_str = sequence
    else:
        bit_str = ''.join(sequence)
    n = len(sequence)
    nr_digits = int(np.log2(modulus))
    vec_min1_plus1 = 2 * np.array(list(map(int, list(bit_str)))) - 1
    sn = np.sum(vec_min1_plus1)
    n_final = int(nr_digits * n)
    sn_final = sn / np.sqrt(n_final)
    normal01 = norm()
    p_value = 2 * (1 - normal01.cdf(np.abs(sn_final)))

    return p_value


def block_test(sequence, M: int) -> float:
    """
    :param sequence: sequence of BITS: ['10', '01', '11']
    :param M: The length of each block
    :return: p_value of test
    """
    sequence = list(map(str, sequence))
    if type(sequence) == str:
        bit_str = sequence
    else:
        bit_str = ''.join(sequence)
    n = len(sequence)
    N = int(np.floor(n / M))
    split_string = [bit_str[i:i + N] for i in range(0, len(bit_str), N)]
    are_not_equaly_splitted = (np.array(list(map(len, split_string))) != 3).sum() != 0

    if are_not_equaly_splitted:
        split_string = split_string[:-1]

    def calc_pi(string):
        return np.array(list(map(int, list(string)))).sum()

    pis = np.array(list(map(calc_pi, split_string))) / M
    chi_stat = 4 * M * ((pis - 1 / 2) ** 2).sum()
    p_value = 1 - gammainc(N / 2, chi_stat / 2)

    return p_value


def ks_test(sequence):
    """
    :param sequence: sequence of BITS: ['10', '01', '11']
    :return: p_value of test
    """
    uni_seq = convert_bit_touni(sequence)
    return kstest(uni_seq, 'uniform')[1]


def runs_test(sequence): #zakladam ze na wejsciu dostajemy ciag zerojedynkowy
    sequence = str(sequence)
    n = len(sequence)
    t = 2/n #tau statistic nie wiem czy sqrt(n) czy n (raz jest tak a raz inaczej w skrypcie)
    # t = 2 / np.sqrt(n)
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


def chi_square_test(f_obs, f_exp=None, ddof=0, axis=0): #wejscie to wektor z liczbami
    return chisquare(f_obs, f_exp, ddof, axis)[1] #p_value
