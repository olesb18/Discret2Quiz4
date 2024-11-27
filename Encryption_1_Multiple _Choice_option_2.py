from sympy import mod_inverse, isprime


def check_rsa_key(x, y, p, q, n):
    if p * q != n:
        print("Invalid: n is not equal to p * q.")
        return False

    if not (isprime(p) and isprime(q)):
        print("Invalid: p and/or q are not prime.")
        return False

    phi_n = (p - 1) * (q - 1)

    try:
        y_inverse = mod_inverse(x, phi_n)
        if y_inverse != y:
            print("Invalid: y is not the modular inverse of x modulo phi(n).")
            return False
    except ValueError:
        print("Invalid: Modular inverse of x does not exist modulo phi(n).")
        return False

    print("Valid RSA key pair!")
    return True

while True:
    x_input = input("Enter x (public exponent, or 'x' to exit): ")
    if x_input.lower() == 'x':
        print("Exiting...")
        break

    try:
        x = int(x_input)
        y = int(input("Enter y (private exponent): "))
        p = int(input("Enter p (prime factor): "))
        q = int(input("Enter q (prime factor): "))
        n = int(input("Enter n (modulus): "))
    except ValueError:
        print("Invalid input! Please enter integers only.")
        continue

    check_rsa_key(x, y, p, q, n)
    print()