text = input("Enter plaintext: ")
key = input("Enter key: ")

result = ""
key = key.upper()
j = 0

for ch in text.upper():
    if ch.isalpha():
        shift = ord(key[j % len(key)]) - ord('A')
        result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        j += 1
    else:
        result += ch

print("Ciphertext:", result)
