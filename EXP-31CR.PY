def subkey(L, n):
    R = 0x1B if n == 64 else 0x87
    K = (L << 1) & ((1 << n) - 1)
    if L >> (n - 1):
        K ^= R
    return K

n = int(input("Enter block size: "))
L = int(input("Enter L in hex: "), 16)

K1 = subkey(L, n)
K2 = subkey(K1, n)

print("K1:", format(K1, f"0{n//4}X"))
print("K2:", format(K2, f"0{n//4}X"))
