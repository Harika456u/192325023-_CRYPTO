import math

ciphertext = input("Enter ciphertext: ").upper()

for a in range(1, 26):
    if math.gcd(a, 26) == 1:
        for b in range(26):
            plaintext = ""
            for ch in ciphertext:
                if ch.isalpha():
                    c = ord(ch) - ord('A')
                    p = (pow(a, -1, 26) * (c - b)) % 26
                    plaintext += chr(p + ord('A'))
                else:
                    plaintext += ch

            print(f"a={a}, b={b}: {plaintext}")
