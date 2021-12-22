from collections import defaultdict
import regex as re
import sys
sys.path.append('..')
import aoc


def solve_part_1(cubes):
    s = 0
    for x1, x2, y1, y2, z1, z2 in cubes:
        if x1 <= 50 and x2 >= -50 and y1 <= 50 and y2 >= -50 and z1 <= 50 and z2 >= -50:
            s += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    return s


def remove_cube(cubes, c_x1, c_x2, c_y1, c_y2, c_z1, c_z2):
    new_cubes = []
    for instr in cubes:
        x1, x2, y1, y2, z1, z2 = instr
        has_overlap = x1 <= c_x2 and x2 >= c_x1 and y1 <= c_y2 and y2 >= c_y1 and z1 <= c_z2 and z2 >= c_z1
        if has_overlap:
            if x1 < c_x1:
                new_cubes.append((x1, c_x1 - 1, y1, y2, z1, z2))
                x1 = c_x1
            if x2 > c_x2:
                new_cubes.append((c_x2 + 1, x2, y1, y2, z1, z2))
                x2 = c_x2
            if y1 < c_y1:
                new_cubes.append((x1,  x2, y1, c_y1 - 1, z1, z2))
                y1 = c_y1
            if y2 > c_y2:
                new_cubes.append((x1, x2, c_y2 + 1, y2, z1, z2))
                y2 = c_y2
            if z1 < c_z1:
                new_cubes.append((x1, x2, y1, y2, z1, c_z1 - 1))
            if z2 > c_z2:
                new_cubes.append((x1, x2, y1, y2, c_z2 + 1, z2))
        else:
            new_cubes.append((x1, x2, y1, y2, z1, z2))
    return new_cubes


def solve_part_2(cubes):
    s = 0
    for x1, x2, y1, y2, z1, z2 in cubes:
        s += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    return s


def solve(instructions):
    cubes = []  # only save cubes that are on here
    for instr in instructions:
        state, x1, x2, y1, y2, z1, z2 = instr
        cubes = remove_cube(cubes, x1, x2, y1, y2, z1, z2)
        if state == 'on':
            cubes.append((x1, x2, y1, y2, z1, z2))
    return cubes


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    instructions = []
    with open(in_f) as f:
        for line in f:
            if not line:
                continue
            state, coords = line.strip().split(' ')
            x1, x2, y1, y2, z1, z2 = aoc.get_ints(coords)
            instructions.append((state, x1, x2, y1, y2, z1, z2))
    cubes = solve(instructions)
    sol1 = solve_part_1(cubes)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(cubes)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
