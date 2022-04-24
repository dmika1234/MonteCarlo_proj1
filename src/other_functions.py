import numpy as np
from functools import partial


def convert_int_tobin(sequence, modulus):
    nr_digits = int(np.log2(modulus))
    mapfunc = partial(np.binary_repr, width=nr_digits)
    res = np.array(list(map(mapfunc, list(sequence))))
    return res


def convert_uni_tobin(sequence, modulus):
    integer_sequence = np.array(np.floor(sequence * modulus), dtype='int32')
    res = convert_int_tobin(integer_sequence, modulus)
    return res


def convert_uni_toint(sequence, modulus):
    integer_sequence = np.array(np.floor(sequence * modulus), dtype='int32')
    return integer_sequence


def convert_int_touni(sequence, modulus):
    res = np.array(sequence) / modulus
    return res


def convert_bit_toint(sequence):
    mapfunc = partial(int, base=2)
    res = np.array(list(map(mapfunc, list(sequence))))
    return res


def convert_bit_touni(sequence):
    nr_digits = len(str(sequence[0]))
    int_lst = convert_bit_toint(sequence)
    res = convert_int_touni(int_lst, 2 ** nr_digits)
    return res


def longint_tobit():
    pass
