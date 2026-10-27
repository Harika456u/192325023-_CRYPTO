
import string

MOD = 26
alphabet = string.ascii_uppercase

# Find modular inverse
def mod_inverse(a, m=26):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

# Inverse of a 2x2 matrix modulo 26
def matrix_inverse(K):
    a, b = K[0]
    c, d = K[1]

    det = (a * d - b * c) % MOD
    inv_det = mod_inverse(det)

    if inv_det is None:
        return None

    return [
        [(d * inv_det) % MOD, (-b * inv_det) % MOD],
        [(-c * inv_det) % MOD, (a * inv_det) % MOD]
    ]

# Multiply matrices modulo 26
def multiply(A, B):
    rows = len(A)
    cols = len(B[0])
    inner = len(B)

    return [
        [
            sum(A[i][k] * B[k][j] for k in range(inner)) % MOD
            for j in range(cols)
        ]
        for i in range(rows)
    ]

# Convert letters to numbers
def text_matrix(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    return [[ord(ch) - ord('A')] for ch in text]

# Known plaintext attack
def recover_key(plain, cipher):
    P = text_matrix(plain)
    C = text_matrix(cipher)

    if len(P) != len(C) or len(P) < 2:
        print("Provide at least two matching letter pairs.")
        return

    # Use the first two pairs as columns
    P2 = [[P[0][0], P[1][0]],
          [P[2][0], P[3][0]]] if len(P) >= 4 else None

    C2 = [[C[0][0], C[1][0]],
          [C[2][0], C[3][0]]] if len(C) >= 4 else None

    if P2 is None:
        print("Not enough letters.")
        return

    P_inv = matrix_inverse(P2)

    if P_inv is None:
        print("Selected plaintext pairs do not form an invertible matrix.")
        print("Try different plaintext letters.")
        return

    K = multiply(C2, P_inv)

    print("Recovered Hill cipher key:")
    for row in K:
        print(row)

    print("\nVerify using all known pairs:")
    print("Recovered key:", K)


# Example: key [[3, 3], [2, 5]]
# Plaintext pairs: HI and AT
# Ciphertext pairs: TC and DP
recover_key("HIAT", "TCDP")
