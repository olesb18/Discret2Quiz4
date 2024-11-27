from math import comb

def probability_at_most_k_errors(p, n, k_max):
    prob = 0
    for k in range(k_max + 1):
        prob += comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return round(prob, 3)

p = 0.051
n = 7
k_max = 2
print("Probability of at most 2 errors:", probability_at_most_k_errors(p, n, k_max))