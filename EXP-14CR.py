
import string

alphabet = string.ascii_lowercase

def encrypt(plaintext, key):
    result = ""
    j = 0

    for ch in plaintext.lower():
        if ch.isalpha():
            p = alphabet.index(ch)
            c = (p + key[j]) % 26
            result += alphabet[c]
            j += 1
        else:
            result += ch

    return result


def decrypt(ciphertext, key):
    result = ""
    j = 0

    for ch in ciphertext.lower():
        if ch.isalpha():
            c = alphabet.index(ch)
            p = (c - key[j]) % 26
            result += alphabet[p]
            j += 1
        else:
            result += ch

    return result


# Part (a)
plaintext = "send more money"
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

ciphertext = encrypt(plaintext, key)

print("Part (a)")
print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)

# Part (b)
target = "cash not needed"

# Derive a key that decrypts the same ciphertext
# into the requested plaintext.
cipher_letters = ''.join(ch for ch in ciphertext if ch.isalpha())
target_letters = ''.join(ch for ch in target if ch.isalpha())

new_key = [
    (alphabet.index(c) - alphabet.index(p)) % 26
    for c, p in zip(cipher_letters, target_letters)
]

print("\nPart (b)")
print("New key   :", new_key)
print("Decrypted :", decrypt(ciphertext, new_key))
