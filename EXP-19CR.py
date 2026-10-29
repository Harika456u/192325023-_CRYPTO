
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Generate 3DES key
key = DES3.adjust_key_parity(get_random_bytes(24))

# Generate IV
iv = get_random_bytes(8)

# Plaintext
plaintext = b"HELLO WORLD"

# Encryption using CBC mode
cipher = DES3.new(key, DES3.MODE_CBC, iv)
ciphertext = cipher.encrypt(
    pad(plaintext, DES3.block_size)
)

print("Plaintext:", plaintext.decode())
print("Encrypted:", ciphertext.hex())

# Decryption
decipher = DES3.new(key, DES3.MODE_CBC, iv)
decrypted = unpad(
    decipher.decrypt(ciphertext),
    DES3.block_size
)

print("Decrypted:", decrypted.decode())
