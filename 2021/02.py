from enum import Enum
from dataclasses import dataclass
from functools import reduce
from typing import Tuple

class InstructionType(Enum):
    UP = 0
    DOWN = 1
    FORWARD = 2

    @staticmethod
    def parse(raw: str):
        if raw == 'up':
            return InstructionType.UP
        if raw == 'down':
            return InstructionType.DOWN
        if raw == 'forward':
            return InstructionType.FORWARD
        raise ValueError('Invalid instruction type')

@dataclass
class Instruction:
    instruction_type: InstructionType
    value: int

    @staticmethod
    def parse(raw: str):
        [ins_type, val] = raw.split(' ')
        return Instruction(
            InstructionType.parse(ins_type),
            int(val)
        )

with open('./input/02.txt') as f:
    instructions = [Instruction.parse(line) for line in f.readlines()]
    print(instructions)

# Task 1
def inc(prev: Tuple[int, int], instruction: Instruction):
    if instruction.instruction_type == InstructionType.UP:
        return (prev[0] - instruction.value, prev[1])
    if instruction.instruction_type == InstructionType.DOWN:
        return (prev[0] + instruction.value, prev[1])
    if instruction.instruction_type == InstructionType.FORWARD:
        return (prev[0], prev[1] + instruction.value)

(vertical, horizontal) = reduce(inc, instructions, (0, 0))

print(vertical * horizontal)

# Task 2
def inc_with_aim(prev: Tuple[int, int, int], instruction: Instruction):
    if instruction.instruction_type == InstructionType.UP:
        return (prev[0], prev[1], prev[2] - instruction.value)
    if instruction.instruction_type == InstructionType.DOWN:
        return (prev[0], prev[1], prev[2] + instruction.value)
    if instruction.instruction_type == InstructionType.FORWARD:
        depth_offset = prev[2] * instruction.value
        return (prev[0] + depth_offset, prev[1] + instruction.value, prev[2])

(vertical, horizontal, _) = reduce(inc_with_aim, instructions, (0, 0, 0))

print(vertical * horizontal)
