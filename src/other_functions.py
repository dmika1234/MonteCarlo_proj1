import numpy as np


def convert_int_tobin(sequence, modulus):
    nr_digits = int(np.log2(modulus))
    converted_sequence = []
    for nr in sequence:
        converted_sequence.append(np.binary_repr(nr, nr_digits))
    return converted_sequence


def convert_uni_tobin(sequence, modulus):
    integer_sequence = np.array(np.floor(sequence * modulus), dtype='int32')
    converted_sequence = convert_int_tobin(integer_sequence, modulus)
    return converted_sequence
