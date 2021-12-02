with open('./input/02.txt') as f:
    instructions = f.readlines()

# Task 1
def sum_instructions(instruction_value):
    return sum([
        instruction_value(ins[:ins.index(' ')], int(ins[ins.index(' ') + 1:]))
        for ins in instructions
    ])

def up_down(cmd, i):
    if cmd == 'up':
        return -i
    elif cmd == 'down':
        return i
    return 0

vertical = sum_instructions(up_down)

horizontal = sum_instructions(lambda cmd, i: i if cmd == 'forward' else 0)

print(vertical * horizontal)
