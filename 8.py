import re

from utils import get_input

instructions = "LRRRLRRLRLLRLRRLRLRLLRRRLRLRRRLRRRLRLRLRRLRLRRRLRRLLRRLLLRRLRRLRRRLRLRRRLRRLRRRLRRRLRRLRLLRRRLRLRRLRLRLRRRLRRLLRRRLLRRLRLRRLRRRLLLRRRLLRLLRRLRRRLRLRLRRLLLRRRLLRRLLLRLRLRRLLRLLRRLLLRRLLRRRLRLRRRLRLLRRRLRRRLRLRLRRRLRLRRRLRRRLRRRLLRLRLRLRRLRLRRRLRLRLLRRLRRLRRLRRRLRRRLRLLRLLLRRLRLRRRR"

instructions_light = "LLR"

"""
AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

import itertools


def prepare_map_dest():
    lines = get_input("inputs/8.txt")
    pattern = re.compile(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)")

    map_dest = {}
    for line in lines:
        for match in pattern.finditer(line):
            key, value1, value2 = match.groups()
            map_dest[key] = (value1, value2)
    return map_dest


def solution():
    target = "ZZZ"
    map_dest = prepare_map_dest()
    instr_map = {
        "L": 0,
        "R": 1,
    }
    start = "AAA"
    count = 0
    cycle = itertools.cycle([s for s in instructions])
    while count < 10_000_000:
        count += 1
        inst = next(cycle)
        dest = map_dest[start][instr_map[inst]]
        if dest == target:
            break
        start = dest

    return count


import math


def part_2():
    _map = prepare_map_dest()
    instr_map = {
        "L": 0,
        "R": 1,
    }
    curr = [node for node in _map.keys() if node.endswith("A")]

    inst_idx = 0
    steps = 0
    inst = instructions

    least_steps = [0] * len(curr)
    while 0 in least_steps:
        for i, node in enumerate(curr):
            if node.endswith("Z") and least_steps[i] == 0:
                least_steps[i] = steps

        curr = [_map[node][instr_map[inst[inst_idx]]] for node in curr]
        inst_idx = (inst_idx + 1) % len(inst)
        steps += 1

    return math.lcm(*least_steps)


print(part_2())
