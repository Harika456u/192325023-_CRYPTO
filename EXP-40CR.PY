from collections import Counter

text = input("Enter ciphertext: ").upper()
n = int(input("Enter number of results: "))
freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

order = ''.join(c for c, v in Counter(
    c for c in text if 'A' <= c <= 'Z').most_common())

for i in range(min(n, 26)):
    f = freq[i:] + freq[:i]
    table = str.maketrans(order, f[:len(order)])
    print(i+1, text.translate(table))
