def probability_no_errors(p, n):
    return round((1 - p) ** n, 3)

p = 0.051
n = 7
print("Probability of no errors:", probability_no_errors(p, n))