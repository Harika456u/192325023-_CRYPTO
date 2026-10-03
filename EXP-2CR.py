text = input("Enter text: ")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

result = ""

for ch in text.upper():
    if ch.isalpha():
        result += key[alphabet.index(ch)]
    else:
        result += ch

print("Ciphertext:", result)
