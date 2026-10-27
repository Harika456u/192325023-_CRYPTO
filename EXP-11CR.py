import math

# Part (a): Total possible keys
total_keys = math.factorial(25)

# Part (b): Effectively unique keys
unique_keys = total_keys // (
    math.factorial(5) * math.factorial(5)
)

print("Total possible keys:", total_keys)
print("Approximate power of 2:",
      round(math.log2(total_keys)))

print("\nEffectively unique keys:", unique_keys)
print("Approximate power of 2:",
      round(math.log2(unique_keys)))
