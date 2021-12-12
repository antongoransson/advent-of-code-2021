from collections import defaultdict
import regex as re


def solve_part_1(in_data):
    pass


def solve_part_2(in_data):
    pass


def main():
    with open('in.txt') as f:
        in_data = map(int, re.findall(r'-?\d+', f.read()))
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')
    
    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
