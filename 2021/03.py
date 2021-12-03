with open('./input/03.txt') as f:
    values = [int(s, base=2) for s in f.readlines()]

# Task 1
LENGTH = 0xFFF

occurences = [0] * LENGTH
for value in values:
    for offset in range(LENGTH):
        if (value >> offset) & 1:
            occurences[offset] += 1

gamma = 0
for offset in range(LENGTH):
    if occurences[offset] > (len(values) / 2):
        gamma |= 1 << offset

epsilon = ~gamma & LENGTH

print(gamma * epsilon)
