import secrets

msg = input("Enter plaintext: ").upper()
key = [secrets.randbelow(26) for i in msg]

enc = ''.join(chr((ord(c)-65+k)%26+65)
              for c,k in zip(msg,key))

dec = ''.join(chr((ord(c)-65-k)%26+65)
              for c,k in zip(enc,key))

print("Key:", key)
print("Encrypted:", enc)
print("Decrypted:", dec)
