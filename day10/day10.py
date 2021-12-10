from functools import reduce

scores_p1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
scores_p2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}
matching_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def calc(t, c):
    return t * 5 + scores_p2[c]


def is_matching_chars(open_c, closing_c):
    return matching_chars[open_c] == closing_c

def test_chunks(line):
    stack = list()
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            opening_c = stack.pop()
            if not is_matching_chars(opening_c, c):
                return [(scores_p1[c], False)]
    return [(reduce(calc, stack[::-1], 0), True)]


def solve_part_1(sub_system):
    return sum(s for line in sub_system for s, ok in test_chunks(line) if not ok)

def solve_part_2(sub_system):
    line_scores = sorted([s for line in sub_system for s, ok in test_chunks(line) if ok])
    return line_scores[(len(line_scores) // 2)]


def main():
    with open('in.txt') as f:
        subsystem = [line.strip() for line in f]
    sol1 = solve_part_1(subsystem)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(subsystem)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
