from collections import defaultdict, Counter, deque
from functools import reduce
import regex as re

scores_p1 = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137 
}
scores_p2 = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4 
}
matching_chars = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>' 
}

def is_matching_chars(open_c, closing_c):
    return matching_chars[open_c] == closing_c

def solve_part_1(sub_system):
    s = 0
    for line in sub_system:
        stack = list()
        for c in line:
            if c in '([{<':
                stack.append(c)
            else:
                opening_c = stack.pop()
                if not is_matching_chars(opening_c, c):
                    s += scores_p1[c]
                    break
    return s

def solve_part_2(sub_system):
    valid_lines = []
    for line in sub_system:
        stack = list()
        ok = True
        for c in line:
            if c in ('([{<'):
                stack.append(c)
            else:
                opening_c = stack.pop()
                if not is_matching_chars(opening_c, c):
                    ok = False
                    break
        if ok:
            valid_lines.append(stack)
    line_scores = []
    for line in valid_lines:
        s = 0
        for c in line[::-1]:
            s = s * 5 + scores_p2[c]
        line_scores.append(s)
    line_scores.sort()
    return line_scores[(len(line_scores) // 2)]

def main():
    with open('in.txt') as f:
        subsystem = [line.strip() for line in f]
    sol1 = solve_part_1(subsystem)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(subsystem)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
