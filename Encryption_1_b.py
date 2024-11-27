def decrypt_message(n, y, encrypted_message):
    plaintext = pow(encrypted_message, y, n)
    return plaintext



n = 2537
y = 451
encrypted_message = 1791
plaintext = decrypt_message(n, y, encrypted_message)
print(f"Decrypted plaintext: {plaintext}")