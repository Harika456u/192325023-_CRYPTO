
# CBC-MAC Attack Demonstration

from Crypto.Cipher import AES

# Step 1: Secret key
key = b'0123456789ABCDEF'

# Step 2: Create AES cipher
cipher = AES.new(key, AES.MODE_ECB)

# Step 3: Define one-block message
X = b'HELLO12345678901'

# Step 4: CBC-MAC function
def cbc_mac(message):
    previous = bytes(16)

    for i in range(0, len(message), 16):
        block = message[i:i+16]
        previous = cipher.encrypt(
            bytes(a ^ b for a, b in zip(block, previous))
        )

    return previous

# Step 5: Calculate MAC for one-block message
T = cbc_mac(X)

print("Original Message X:", X)
print("CBC-MAC of X:", T.hex())

# Step 6: Construct second block (X XOR T)
second_block = bytes(a ^ b for a, b in zip(X, T))

# Step 7: Construct two-block message
forged_message = X + second_block

print("\nForged Two-Block Message:", forged_message.hex())

# Step 8: Calculate MAC of forged message
forged_mac = cbc_mac(forged_message)

print("MAC of Two-Block Message:", forged_mac.hex())

# Step 9: Verify the attack
if T == forged_mac:
    print("\nAttack Successful!")
    print("Both MAC values are identical.")
else:
    print("\nAttack Failed!")
