
from collections import Counter
import string

# English letter frequency
frequency = "etaoinshrdlcumwfgypbvkjxqz"

def frequency_attack(cipher, top=10):
    cipher = cipher.upper()
    letters = [c for c in cipher if c.isalpha()]

    # Count letter frequency
    counts = Counter(letters)

    # Sort letters by frequency
    sorted_letters = sorted(
        counts, key=counts.get, reverse=True
    )

    # Create substitution mapping
    mapping = {
        sorted_letters[i]: frequency[i].upper()
        for i in range(min(len(sorted_letters), 26))
    }

    # Generate possible plaintext
    plaintext = ''.join(
        mapping.get(c, c) for c in cipher
    )

    print("\nTop", top, "possible plaintexts:")

    for i in range(top):
        print(i + 1, ".", plaintext)

        # Change mapping to generate alternatives
        if len(sorted_letters) > 1:
            a = sorted_letters[i % len(sorted_letters)]
            b = sorted_letters[(i + 1) % len(sorted_letters)]

            mapping[a], mapping[b] = mapping[b], mapping[a]

            plaintext = ''.join(
                mapping.get(c, c) for c in cipher
            )

# Input ciphertext
cipher = input("Enter ciphertext: ")

top = int(input("Enter number of plaintexts: "))

frequency_attack(cipher, top)
