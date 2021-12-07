import regex as re


def solve_part_1(crabs):
    return min(sum(abs(k - i) for k in crabs) for i in range(max(crabs) + 1))


def solve_part_2(crabs):
    return min(sum(abs(k - i) * (abs(k - i) + 1) // 2 for k in crabs) for i in range(max(crabs) + 1))


def main():
    with open('in.txt') as f:
        crabs = list(map(int, re.findall(r'-?\d+', f.read())))
    sol1 = solve_part_1(crabs)
    print('Part 1: {}'.format(sol1))

    sol2 = solve_part_2(crabs)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
