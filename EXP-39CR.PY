text = input("Enter ciphertext: ").upper()
n = int(input("Enter number of results: "))
freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
results = []

for k in range(26):
    p = ''.join(chr((ord(c)-65-k)%26+65)
                if 'A' <= c <= 'Z' else c for c in text)
    score = sum(26-freq.index(c) for c in p if c in freq)
    results.append((score, k, p))

for s, k, p in sorted(results, reverse=True)[:n]:
    print("Key:", k, "Plaintext:", p)
