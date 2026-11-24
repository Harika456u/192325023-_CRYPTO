from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'12345678'
msg = input("Enter plaintext: ").encode()

cipher = DES.new(key, DES.MODE_ECB)
enc = cipher.encrypt(pad(msg, 8))
dec = unpad(cipher.decrypt(enc), 8)

print("Encrypted:", enc.hex())
print("Decrypted:", dec.decode())
