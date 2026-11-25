from math import gcd

p = input("Enter plaintext: ").upper()
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if gcd(a, 26) != 1:
    print("Invalid key: Encryption is not one-to-one")
else:
    c = ""
    for ch in p:
        if 'A' <= ch <= 'Z':
            c += chr((a * (ord(ch)-65) + b) % 26 + 65)
        else:
            c += ch
    print("Ciphertext:", c)
