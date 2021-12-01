with open('./input/01.txt') as f:
    lines = [int(l) for l in f.readlines()]

# Part 1
increasing = 0
for idx in range(1, len(lines)):
    if lines[idx - 1] < lines[idx]:
        increasing += 1

print('Increasing: ' + str(increasing))

# Part 2
increasing = 0
for idx in range(3, len(lines)):
    if sum(lines[idx - 4:idx-1]) < sum(lines[idx - 3:idx]):
        increasing += 1

print('Increasing (sliding window): ' + str(increasing))
