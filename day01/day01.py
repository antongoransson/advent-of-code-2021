import regex as re


def solve_part_1(depths):
    return len([1 for i in range(1, len(depths)) if depths[i] > depths[i - 1]])


def solve_part_2(depths):
    return len([1 for i in range(1, len(depths)) if sum(depths[i: i + 3]) > sum(depths[i - 1: i + 2])])


def main():
    with open('input.txt') as f:
        in_data = list(map(int, re.findall(r'-?\d+', f.read())))
    sol1 = solve_part_1(in_data)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(in_data)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
