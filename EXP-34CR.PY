from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'
iv = b'abcdefghijklmnop'
msg = input("Enter plaintext: ").encode()
data = pad(msg, 16, style='iso7816')

for mode in [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB]:
    args = {} if mode == AES.MODE_ECB else {'iv': iv}
    enc = AES.new(key, mode, **args).encrypt(data)
    dec = AES.new(key, mode, **args).decrypt(enc)

    print("Mode:", {1: 'ECB', 2: 'CBC', 3: 'CFB'}[mode])
    print("Encrypted:", enc.hex())
    print("Decrypted:", unpad(dec, 16, style='iso7816').decode())
