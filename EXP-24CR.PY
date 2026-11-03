
# RSA Key Generation, Encryption and Decryption

# Given public key
e = 31
n = 3599

# Step 1: Find p and q
p = 59
q = 61

# Step 2: Calculate Euler's Totient
phi = (p - 1) * (q - 1)

# Step 3: Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y

# Step 4: Find private key d
gcd, x, y = extended_gcd(e, phi)

d = x % phi

print("RSA PARAMETERS")
print("p =", p)
print("q =", q)
print("n =", n)
print("Euler Totient =", phi)
print("Public Key =", (e, n))
print("Private Key =", (d, n))

# Step 5: Encryption
message = 123

cipher = pow(message, e, n)

print("\nOriginal Message:", message)
print("Encrypted Message:", cipher)

# Step 6: Decryption
decrypted = pow(cipher, d, n)

print("Decrypted Message:", decrypted)
