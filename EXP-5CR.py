def affine_cipher(text, a, b):
    result = ""

    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if 0 <= b < 26 and 0 <= a < 26:
    import math
    if math.gcd(a, 26) == 1:
        print("Ciphertext:", affine_cipher(text, a, b))
    else:
        print("Invalid value of a. GCD(a, 26) must be 1.")
else:
    print("Enter a and b between 0 and 25.")
