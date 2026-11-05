
# RSA Encryption and Decryption

import math

# Step 1: Choose two prime numbers
p = 61
q = 53

# Step 2: Calculate modulus
n = p * q

# Step 3: Calculate Euler's Totient
phi = (p - 1) * (q - 1)

# Step 4: Choose public key e
e = 17

# Step 5: Calculate private key d
d = pow(e, -1, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Step 6: Encryption
message = 65
ciphertext = pow(message, e, n)

print("\nOriginal Message:", message)
print("Encrypted Message:", ciphertext)

# Step 7: Decryption
decrypted = pow(ciphertext, d, n)

print("Decrypted Message:", decrypted)

# Bob's private key is leaked
print("\n--- Private Key Leakage ---")
print("Bob's private key is leaked!")

# Generate a new public and private exponent
new_e = 7
new_d = pow(new_e, -1, phi)

print("New Public Key:", (new_e, n))
print("New Private Key:", (new_d, n))

print("\nModulus remains unchanged:", n)
print("Changing only e and d is NOT safe.")
