def caesar_cipher(text, k):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char

    return result


text = input("Enter the message: ")
k = int(input("Enter the key (1-25): "))

if 1 <= k <= 25:
    encrypted = caesar_cipher(text, k)
    print("Encrypted message:", encrypted)
else:
    print("Key must be between 1 and 25.")
