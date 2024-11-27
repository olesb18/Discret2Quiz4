import numpy as np
from itertools import combinations

G = np.array([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1]
], dtype=int)


def encode(w):
    return np.dot(w, G) % 2


def compute_codewords():
    codewords = []
    for w1 in [0, 1]:
        for w2 in [0, 1]:
            for w3 in [0, 1]:
                w = np.array([w1, w2, w3], dtype=int)
                codewords.append(encode(w))
    return codewords

def compute_min_distance(codewords):
    min_distance = float('inf')
    for cw1, cw2 in combinations(codewords, 2):
        distance = np.sum(cw1 != cw2)  # Hamming distance
        if distance < min_distance:
            min_distance = distance
    return min_distance

codewords = compute_codewords()
l_min = compute_min_distance(codewords)
print("Minimum distance (l_min):", l_min)