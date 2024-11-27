from math import comb

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def probability_exactly_k_errors(p, n, k):
    return round(comb(n, k) * (p ** k) * ((1 - p) ** (n - k)), 3)

p = 0.051
w = "1011010"
r = "1000010"
n = len(w)
k = hamming_distance(w, r)
print("Probability of transmitting w and receiving r:", probability_exactly_k_errors(p, n, k))