import random

p, q, g, x = 23, 11, 4, 3
m = 9

def dsa(k):
    r = pow(g, k, p) % q
    s = (pow(k, -1, q) * (m + x*r)) % q
    return r, s

k1, k2 = random.sample(range(1, q), 2)

print("DSA Signature 1:", dsa(k1))
print("DSA Signature 2:", dsa(k2))

n, d = 3233, 2753

print("RSA Signature 1:", pow(m, d, n))
print("RSA Signature 2:", pow(m, d, n))
