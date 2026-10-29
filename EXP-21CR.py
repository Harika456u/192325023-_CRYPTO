
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'
iv = b'1234567890123456'

plaintext = b'HELLO WORLD'

# Padding
data = pad(plaintext, AES.block_size)

# ECB Mode
ecb = AES.new(key, AES.MODE_ECB)
ecb_enc = ecb.encrypt(data)
ecb_dec = AES.new(key, AES.MODE_ECB).decrypt(ecb_enc)

# CBC Mode
cbc = AES.new(key, AES.MODE_CBC, iv)
cbc_enc = cbc.encrypt(data)
cbc_dec = AES.new(key, AES.MODE_CBC, iv).decrypt(cbc_enc)

# CFB Mode
cfb = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
cfb_enc = cfb.encrypt(plaintext)
cfb_dec = AES.new(
    key, AES.MODE_CFB, iv, segment_size=128
).decrypt(cfb_enc)

print("Plaintext:", plaintext.decode())

print("\nECB Mode")
print("Encrypted:", ecb_enc.hex())
print("Decrypted:", unpad(ecb_dec, 16).decode())

print("\nCBC Mode")
print("Encrypted:", cbc_enc.hex())
print("Decrypted:", unpad(cbc_dec, 16).decode())

print("\nCFB Mode")
print("Encrypted:", cfb_enc.hex())
print("Decrypted:", cfb_dec.decode())
