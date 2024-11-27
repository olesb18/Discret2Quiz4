def encode(w1, w2, w3):
    w4 = w3
    w5 = (w3 + w2) % 2
    return f"{w1}{w2}{w3}{w4}{w5}"

def find_specific_codeword():
    w1, w2, w3 = 1, 0, 0
    return encode(w1, w2, w3)

specific_codeword = find_specific_codeword()
print("c = ", specific_codeword)