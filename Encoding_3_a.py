from itertools import product

def encode(w1, w2, w3):
    w4 = w3
    w5 = (w3 + w2) % 2  # Modulo 2 arithmetic
    return (w1, w2, w3, w4, w5)

def hamming_distance(codeword1, codeword2):
    return sum(c1 != c2 for c1, c2 in zip(codeword1, codeword2))

def compute_min_hamming_distance():

    inputs = product([0, 1], repeat=3)

    codewords = [encode(w1, w2, w3) for w1, w2, w3 in inputs]

    min_distance = float('inf')
    for i, cw1 in enumerate(codewords):
        for j, cw2 in enumerate(codewords):
            if i < j:
                distance = hamming_distance(cw1, cw2)
                if distance < min_distance:
                    min_distance = distance

    return min_distance

d_min = compute_min_hamming_distance()
print("Minimum Hamming distance (d_min):", d_min)
print("Maximum number of detectable errors:", d_min - 1)