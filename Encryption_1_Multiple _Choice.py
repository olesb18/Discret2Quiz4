from sympy import mod_inverse, isprime

def is_valid_prime_pair(p, q):
    return isprime(p) and isprime(q)

def find_correct_rsa_keys(key_candidates):
    valid_keys = []
    for x, y, p, q, n in key_candidates:
        n_valid = (p * q == n)
        primes_valid = is_valid_prime_pair(p, q)

        if n_valid and primes_valid:
            phi_n = (p - 1) * (q - 1)
            try:
                y_inverse = mod_inverse(x, phi_n)
                y_valid = (y_inverse == y)
            except ValueError:
                y_valid = False

            if y_valid:
                valid_keys.append((x, y, p, q, n))

    return valid_keys


# Example key candidates
key_candidates = [
    (2124966, 1889417, 5477, 2437, 13347449),
    (14024123, 3588467, 3879, 6529, 25325991),
    (35519203, 9772867, 5471, 7351, 40217321),
    (3872401, 5158441, 7247, 4261, 30879467),
    (36784094, 14173807, 6833, 6823, 46621559),
    (2846781, 2055541, 2709, 2861, 7750449),
]

# Find the correct RSA keys
correct_keys = find_correct_rsa_keys(key_candidates)

# Print the results
print("Correct RSA Key Pairs with Valid Primes:")
for x, y, p, q, n in correct_keys:
    print(f"x = {x}, y = {y}, p = {p}, q = {q}, n = {n}")