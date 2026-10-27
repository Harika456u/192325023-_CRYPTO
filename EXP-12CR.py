
import string

alphabet = string.ascii_uppercase

# Key matrix
K = [[9, 4],
     [5, 7]]

# Inverse key matrix modulo 26
K_inv = [[5, 12],
         [15, 25]]


def prepare_text(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    text = text.replace('J', 'I')

    if len(text) % 2 != 0:
        text += 'X'

    return text


def encrypt(text):
    text = prepare_text(text)
    result = ''

    for i in range(0, len(text), 2):
        p1 = ord(text[i]) - ord('A')
        p2 = ord(text[i + 1]) - ord('A')

        c1 = (K[0][0] * p1 + K[0][1] * p2) % 26
        c2 = (K[1][0] * p1 + K[1][1] * p2) % 26

        result += chr(c1 + ord('A'))
        result += chr(c2 + ord('A'))

    return result


def decrypt(ciphertext):
    result = ''

    for i in range(0, len(ciphertext), 2):
        c1 = ord(ciphertext[i]) - ord('A')
        c2 = ord(ciphertext[i + 1]) - ord('A')

        p1 = (K_inv[0][0] * c1 + K_inv[0][1] * c2) % 26
        p2 = (K_inv[1][0] * c1 + K_inv[1][1] * c2) % 26

        result += chr(p1 + ord('A'))
        result += chr(p2 + ord('A'))

    return result


message = "meet me at the usual place at ten rather than eight oclock"

ciphertext = encrypt(message)

print("Original message:", message)
print("Encrypted message:", ciphertext)
print("Decrypted message:", decrypt(ciphertext))
