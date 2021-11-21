from collections import defaultdict
import regex as re


def solve_part_1(in_data):
    pass


def solve_part_2(in_data):
    pass


def main():
    with open('input.txt') as f:
        in_data = map(int, re.findall(r'-?\d+', f))
    sol1 = solve_part_1(in_data)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(in_data)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
