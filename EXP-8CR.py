
import string

keyword = "CIPHER"
alphabet = string.ascii_uppercase

# Create cipher alphabet using keyword
cipher_alphabet = ""
for ch in keyword + alphabet:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch

print("Plain alphabet :", alphabet)
print("Cipher alphabet:", cipher_alphabet)

plaintext = input("Enter plaintext: ").upper()
ciphertext = ""

for ch in plaintext:
    if ch in alphabet:
        ciphertext += cipher_alphabet[alphabet.index(ch)]
    else:
        ciphertext += ch

print("Ciphertext:", ciphertext)
