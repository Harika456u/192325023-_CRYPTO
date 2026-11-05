
# RSA Encryption of Alphabetic Characters

# Step 1: Select two prime numbers
p = 61
q = 53

# Step 2: Calculate modulus and Euler's totient
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Generate public and private keys
e = 17
d = pow(e, -1, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Step 4: Input message
message = input("Enter a message: ").upper()

# Step 5: Convert characters into numbers
numbers = []

for ch in message:
    if ch.isalpha():
        numbers.append(ord(ch) - ord('A'))

print("\nCharacter to Number Conversion:")
print(numbers)

# Step 6: Encrypt each character separately
encrypted = [pow(num, e, n) for num in numbers]

print("\nEncrypted Message:")
print(encrypted)

# Step 7: Decrypt the message
decrypted = [pow(num, d, n) for num in encrypted]

# Step 8: Convert numbers back into characters
result = ''.join(chr(num + ord('A')) for num in decrypted)

print("\nDecrypted Message:", result)

# Step 9: Demonstrate security weakness
print("\n--- Security Analysis ---")
print("Each alphabet has a fixed numerical value.")
print("The same character always produces the same ciphertext.")
print("Therefore, this method is NOT secure.")
print("Frequency analysis and codebook attacks can reveal the message.")
