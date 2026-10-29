
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'
iv = b'1234567890123456'

plaintext = b'ABCDEFGHIJKLMNOPQRSTUVWX12345678'

# ECB Encryption
ecb = AES.new(key, AES.MODE_ECB)
ecb_cipher = ecb.encrypt(pad(plaintext, 16))

# CBC Encryption
cbc = AES.new(key, AES.MODE_CBC, iv)
cbc_cipher = cbc.encrypt(pad(plaintext, 16))

# Introduce error in first ciphertext block
ecb_error = bytearray(ecb_cipher)
ecb_error[0] ^= 1

cbc_error = bytearray(cbc_cipher)
cbc_error[0] ^= 1

# ECB Decryption
ecb_dec = AES.new(key, AES.MODE_ECB)
ecb_plain = ecb_dec.decrypt(bytes(ecb_error))

# CBC Decryption
cbc_dec = AES.new(key, AES.MODE_CBC, iv)
cbc_plain = cbc_dec.decrypt(bytes(cbc_error))

print("Original Plaintext:", plaintext.decode())

print("\nECB Error Decryption:")
print(ecb_plain.decode(errors="replace"))

print("\nCBC Error Decryption:")
print(cbc_plain.decode(errors="replace"))

print("\nECB Ciphertext:", ecb_cipher.hex())
print("CBC Ciphertext:", cbc_cipher.hex())
