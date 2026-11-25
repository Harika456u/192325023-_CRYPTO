from collections import Counter

text = input("Enter ciphertext: ").upper()
n = int(input("Number of possible plaintexts: "))
freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

letters = Counter(c for c in text if 'A' <= c <= 'Z')
order = ''.join(c for c, _ in letters.most_common())

for i in range(min(n, 26)):
    f = freq[i:] + freq[:i]
    table = str.maketrans(order, f[:len(order)])
    print(i+1, text.translate(table))
