import numpy as np
from itertools import combinations

G = np.array([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1]
], dtype=int)


def encode(w):
    return np.dot(w, G) % 2


def find_non_zero_codeword():

    w = np.array([1, 0, 0], dtype=int)  # Example non-zero input
    return encode(w)


# Generate and print a non-zero codeword
non_zero_codeword = find_non_zero_codeword()
print("Non-zero codeword (c):", ''.join(map(str, non_zero_codeword)))