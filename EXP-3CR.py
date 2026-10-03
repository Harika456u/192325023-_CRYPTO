def create_matrix(key):
    key = key.upper().replace("J", "I")
    chars = ""

    for ch in key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in chars:
            chars += ch

    return [chars[i:i+5] for i in range(0, 25, 5)]


def prepare_text(text):
    text = text.upper().replace("J", "I")
    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"

        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2

    return result


def encrypt(text, matrix):
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    r1, c1 = r, c
                if matrix[r][c] == b:
                    r2, c2 = r, c

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
text = input("Enter plaintext: ")

matrix = create_matrix(key)
text = prepare_text(text)

print("Encrypted text:", encrypt(text, matrix))
