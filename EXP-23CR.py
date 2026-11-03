
# Classical and Modern Encryption Techniques
# Caesar, Playfair, Vigenere and AES

import string
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Given plaintext
plaintext = "CONFIDENTIALDATA"


# 1. CAESAR CIPHER
def caesar_encrypt(text, shift):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# 2. PLAYFAIR CIPHER
def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    chars = []

    for ch in key + alphabet:
        if ch.isalpha() and ch not in chars:
            chars.append(ch)

    return [chars[i:i + 5] for i in range(0, 25, 5)]


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(ch for ch in text if ch.isalpha())

    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]
        else:
            b = 'X'

        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    return pairs


def playfair(text, key, decrypt=False):
    matrix = create_matrix(key)

    def position(ch):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == ch:
                    return r, c

    result = ""

    for pair in prepare_text(text):
        a, b = pair
        r1, c1 = position(a)
        r2, c2 = position(b)

        shift = -1 if decrypt else 1

        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5]
            result += matrix[r2][(c2 + shift) % 5]

        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1]
            result += matrix[(r2 + shift) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


# 3. VIGENERE CIPHER
def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch) - 65 - shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result


# 4. AES SYMMETRIC ENCRYPTION
def aes_encrypt(text, key):
    # Derive a 256-bit key from the password
    aes_key = hashlib.sha256(key.encode()).digest()

    # Generate a random initialization vector
    iv = get_random_bytes(16)

    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    encrypted = cipher.encrypt(
        pad(text.encode(), AES.block_size)
    )

    return iv + encrypted


def aes_decrypt(ciphertext, key):
    aes_key = hashlib.sha256(key.encode()).digest()

    iv = ciphertext[:16]
    encrypted = ciphertext[16:]

    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    decrypted = unpad(
        cipher.decrypt(encrypted),
        AES.block_size
    )

    return decrypted.decode()


# MAIN PROGRAM
print("Original Plaintext:", plaintext)

# Caesar
caesar_key = 7
c = caesar_encrypt(plaintext, caesar_key)
print("\nCaesar Cipher")
print("Encrypted:", c)
print("Decrypted:", caesar_decrypt(c, caesar_key))

# Playfair
playfair_key = "SECURITY"
p = playfair(plaintext, playfair_key)
print("\nPlayfair Cipher")
print("Encrypted:", p)
print("Decrypted:", playfair(p, playfair_key, True))

# Vigenere
vigenere_key = "NETWORK"
v = vigenere_encrypt(plaintext, vigenere_key)
print("\nVigenere Cipher")
print("Encrypted:", v)
print("Decrypted:", vigenere_decrypt(v, vigenere_key))

# AES
aes_key = "FinancialSecureKey"
a = aes_encrypt(plaintext, aes_key)
print("\nAES Encryption")
print("Encrypted (Hex):", a.hex())
print("Decrypted:", aes_decrypt(a, aes_key))
