
# SHA-3 Capacity Lane Analysis

# SHA-3 state size = 1600 bits
# Block size = 1024 bits
# Capacity = 1600 - 1024 = 576 bits
# Each lane = 64 bits

state_size = 1600
block_size = 1024
lane_size = 64

capacity = state_size - block_size
capacity_lanes = capacity // lane_size

# Initial capacity lanes contain zero bits
zero_lanes = capacity_lanes

# Each message block has 1024 bits = 16 lanes
message_lanes = block_size // lane_size

print("SHA-3 State Size:", state_size, "bits")
print("Block Size:", block_size, "bits")
print("Capacity:", capacity, "bits")
print("Capacity Lanes:", capacity_lanes)
print("Message Lanes:", message_lanes)

# Count message blocks needed
blocks = 0

while zero_lanes > 0:
    blocks += 1
    zero_lanes -= min(message_lanes, zero_lanes)

    print("After block", blocks,
          "remaining zero capacity lanes:", zero_lanes)

print("\nTotal Message Blocks Required:", blocks)
print("All capacity lanes now contain nonzero bits.")
