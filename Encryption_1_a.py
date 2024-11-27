from sympy import mod_inverse, primefactors


def find_private_key(n, e):
    factors = primefactors(n)
    if len(factors) != 2:
        raise ValueError("n should be a product of two primes.")
    p, q = factors[0], factors[1]
    phi_n = (p - 1) * (q - 1)
    y = mod_inverse(e, phi_n)
    return p, q, phi_n, y


n = 2537
e = 1615
p, q, phi_n, y = find_private_key(n, e)
print(f"p: {p}, q: {q}, phi(n): {phi_n}, y (private key): {y}")