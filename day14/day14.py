from collections import Counter
import sys

def solve(n_steps, rules, pairs):
    for t in range(n_steps):
        new_pairs = Counter()
        for p, c in pairs.items():
            new_pairs[p[0] + rules[p]] += c
            new_pairs[rules[p] + p[1]] += c
        pairs = new_pairs
    char_count = Counter()
    for (f, s), c in pairs.items():
        char_count[f] += c
        char_count[s] += c
    max_c, min_c = char_count.most_common()[0], char_count.most_common()[-1]
    return (max_c[1] - min_c[1]) // 2 + 1


def solve_part_1(rules, pairs):
    return solve(10, rules, pairs)


def solve_part_2(rules, pairs):
    return solve(40, rules, pairs)

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    rules = {}
    pairs = Counter()
    with open(in_f) as f:
        lines = f.readlines()
        template = list(lines[0].strip())
        for line in lines[2:]:
            p, c = line.split('->')
            rules[p.strip()] = c.strip()
        for i in range(1, len(template)):
            pairs[template[i - 1] + template[i]] += 1
    sol1 = solve_part_1(rules, pairs)
    print(f'Part 1: {sol1}')
    sol2 = solve_part_2(rules, pairs)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
