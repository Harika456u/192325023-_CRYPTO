
# Diffie-Hellman Key Exchange Protocol

# Step 1: Public parameters
q = 23
a = 5

# Step 2: Secret keys of Alice and Bob
x = 6       # Alice's private key
y = 15      # Bob's private key

# Step 3: Calculate public keys
A = pow(a, x, q)
B = pow(a, y, q)

print("Public Prime (q):", q)
print("Public Base (a):", a)

print("\nAlice's Secret Key:", x)
print("Bob's Secret Key:", y)

print("\nAlice's Public Key:", A)
print("Bob's Public Key:", B)

# Step 4: Exchange public keys
# Step 5: Calculate shared secret key
alice_key = pow(B, x, q)
bob_key = pow(A, y, q)

print("\nAlice's Shared Key:", alice_key)
print("Bob's Shared Key:", bob_key)

# Step 6: Verify shared keys
if alice_key == bob_key:
    print("\nShared Secret Key Established Successfully!")
else:
    print("\nKey Exchange Failed!")

# Step 7: Alternative method using x^a
print("\n--- Alternative Method ---")
alice_value = x ** a
bob_value = y ** a

print("Alice sends x^a:", alice_value)
print("Bob sends y^a:", bob_value)

print("\nThese values do not provide the standard")
print("Diffie-Hellman shared-key property.")
