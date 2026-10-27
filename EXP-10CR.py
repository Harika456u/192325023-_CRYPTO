matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

def find_position(ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def encrypt_pair(a, b):
    r1, c1 = find_position(a)
    r2, c2 = find_position(b)

    # Same row
    if r1 == r2:
        return (matrix[r1][(c1 + 1) % 5] +
                matrix[r2][(c2 + 1) % 5])

    # Same column
    elif c1 == c2:
        return (matrix[(r1 + 1) % 5][c1] +
                matrix[(r2 + 1) % 5][c2])

    # Rectangle rule
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def encrypt_message(message):
    message = ''.join(
        ch for ch in message.upper() if ch.isalpha()
    ).replace('J', 'I')

    pairs = []
    i = 0

    while i < len(message):
        a = message[i]

        if i + 1 >= len(message):
            b = 'X'
            i += 1
        elif message[i] == message[i + 1]:
            b = 'X'
            i += 1
        else:
            b = message[i + 1]
            i += 2

        pairs.append(a + b)

    print("Plaintext pairs:", ' '.join(pairs))

    ciphertext = ""
    for pair in pairs:
        ciphertext += encrypt_pair(pair[0], pair[1])

    return ciphertext

message = "Must see you over Cadogan West. Coming at once."

print("Plaintext:", message)
print("Ciphertext:", encrypt_message(message))
