
from collections import Counter

# Approximate English letter frequencies
english_freq = {
    'a': 8.12, 'b': 1.49, 'c': 2.71, 'd': 4.32,
    'e': 12.02, 'f': 2.30, 'g': 2.03, 'h': 5.92,
    'i': 7.31, 'j': 0.10, 'k': 0.69, 'l': 3.98,
    'm': 2.61, 'n': 6.95, 'o': 7.68, 'p': 1.82,
    'q': 0.11, 'r': 6.02, 's': 6.28, 't': 9.10,
    'u': 2.88, 'v': 1.11, 'w': 2.09, 'x': 0.17,
    'y': 2.11, 'z': 0.07
}

def decrypt(ciphertext, key):
    plaintext = ""

    for ch in ciphertext:
        if ch.isupper():
            plaintext += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
        elif ch.islower():
            plaintext += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            plaintext += ch

    return plaintext


def score_text(text):
    letters = [ch.lower() for ch in text if ch.isalpha()]
    if not letters:
        return float("-inf")

    counts = Counter(letters)
    total = len(letters)

    # Chi-squared score: smaller is better
    score = 0

    for letter, expected_percent in english_freq.items():
        expected = total * expected_percent / 100
        observed = counts.get(letter, 0)

        if expected > 0:
            score += (observed - expected) ** 2 / expected

    return score


ciphertext = input("Enter ciphertext: ")
top_n = int(input("How many top plaintexts (1-26)? "))

if not 1 <= top_n <= 26:
    print("Enter a number between 1 and 26.")
else:
    candidates = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = score_text(plaintext)
        candidates.append((score, key, plaintext))

    # Lower chi-squared score means a better frequency match
    candidates.sort(key=lambda item: item[0])

    print("\nTop possible plaintexts:")

    for rank, (score, key, plaintext) in enumerate(
        candidates[:top_n], start=1
    ):
        print(f"\nRank {rank} | Key = {key}")
        print("Plaintext:", plaintext)
