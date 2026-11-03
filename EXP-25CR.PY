
# RSA Common Factor Attack

import math

# RSA public key
e = 31
n = 3599

# Plaintext blocks
blocks = [123, 59, 61, 100, 200]

print("RSA Common Factor Attack")
print("Public Key:", (e, n))

for m in blocks:

    # Find common factor
    factor = math.gcd(m, n)

    print("\nPlaintext Block:", m)
    print("GCD with n:", factor)

    if 1 < factor < n:

        # Factorization of n
        p = factor
        q = n // p

        # Calculate Euler's totient
        phi = (p - 1) * (q - 1)

        # Calculate private key
        d = pow(e, -1, phi)

        print("Factor p =", p)
        print("Factor q =", q)
        print("Euler Totient =", phi)
        print("Private Key d =", d)

        print("RSA Private Key:", (d, n))

    else:
        print("No useful factor found")
