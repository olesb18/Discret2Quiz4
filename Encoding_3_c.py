from itertools import product

def is_codeword(w1, w2, w3, w4, w5):
    return w4 == w3 and w5 == (w3 + w2) % 2

def find_all_non_codewords():
    non_codewords = []
    for bits in product([0, 1], repeat=5):
        w1, w2, w3, w4, w5 = bits
        if not is_codeword(w1, w2, w3, w4, w5):
            non_codewords.append(f"{w1}{w2}{w3}{w4}{w5}")
    return non_codewords

all_non_codewords = find_all_non_codewords()
print("All non-codewords:")
print(all_non_codewords)