
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Key generation
key = b'12345678'

# Plaintext
plaintext = b'HELLO DES'

# Encryption
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

print("Encrypted Text:", ciphertext.hex())

# Decryption using reverse round keys
decrypt_cipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(
    decrypt_cipher.decrypt(ciphertext),
    DES.block_size
)

print("Decrypted Text:", decrypted.decode())
