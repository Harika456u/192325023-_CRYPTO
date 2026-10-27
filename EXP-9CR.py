def generate_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    chars = ""
    for ch in key + alphabet:
        if ch.isalpha() and ch not in chars:
            chars += ch

    return [list(chars[i:i+5]) for i in range(0, 25, 5)]


def find_position(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


def decrypt_pair(matrix, a, b):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + \
               matrix[r2][(c2 - 1) % 5]

    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + \
               matrix[(r2 - 1) % 5][c2]

    else:
        return matrix[r1][c2] + matrix[r2][c1]


def playfair_decrypt(ciphertext, key):
    matrix = generate_matrix(key)
    ciphertext = "".join(
        ch for ch in ciphertext.upper() if ch.isalpha()
    ).replace("J", "I")

    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(
            matrix, ciphertext[i], ciphertext[i + 1]
        )

    return matrix, plaintext


ciphertext = """
KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ
"""

key = input("Enter Playfair key: ")

matrix, plaintext = playfair_decrypt(ciphertext, key)

print("\nPlayfair Matrix:")
for row in matrix:
    print(" ".join(row))

print("\nDecrypted message:")
print(plaintext)
