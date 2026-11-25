c1 = input("Enter ciphertext for BA: ").upper()
c2 = input("Enter ciphertext for AB: ").upper()

print("Recovered Key Matrix:")
print(ord(c1[0])-65, ord(c2[0])-65)
print(ord(c1[1])-65, ord(c2[1])-65)
