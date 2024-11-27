from itertools import combinations

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def compute_min_max_hamming(bitstrings):
    distances = []
    for s1, s2 in combinations(bitstrings, 2):
        distances.append(hamming_distance(s1, s2))

    return min(distances), max(distances)


bitstrings = ["000010", "010000", "001001", "000100"]
l_min, l_max = compute_min_max_hamming(bitstrings)
print(f"l_min = {l_min}")
print(f"l_max = {l_max}")
