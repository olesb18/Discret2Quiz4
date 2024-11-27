import numpy as np

from EncodingMatrix_3_a import codewords

G = np.array([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1]
], dtype=int)


def encode(w):
    return np.dot(w, G) % 2


def is_codeword(x, codewords):
    for codeword in codewords:
        if np.array_equal(x, codeword):
            return True
    return False


def find_non_codeword(codewords):
    for x1 in [0, 1]:
        for x2 in [0, 1]:
            for x3 in [0, 1]:
                for x4 in [0, 1]:
                    for x5 in [0, 1]:
                        x = np.array([x1, x2, x3, x4, x5], dtype=int)
                        if not is_codeword(x, codewords):
                            return x

non_codeword = find_non_codeword(codewords)
print("Non-codeword (x):", ''.join(map(str, non_codeword)))