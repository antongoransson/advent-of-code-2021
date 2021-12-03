from collections import defaultdict, Counter


def get_rating(l, b1, b2):
    i = 0
    while len(l) > 1:
        count = get_count(l)
        bit = b1 if count[i]['0'] <= count[i]['1'] else b2
        l = [b for b in l if b[i] == bit]
        i += 1
    return l[0]


def get_count(in_data):
    count = defaultdict(Counter)
    for binary in in_data:
        for i, c in enumerate(binary):
            count[i][c] += 1
    return count


def solve_part_1(in_data):
    count = get_count(in_data)
    gamma = ''.join('0' if c['0'] > c['1'] else '1' for c in count.values())
    epsilon = ''.join('1' if c['0'] > c['1'] else '0' for c in count.values())
    return int(gamma, 2) * int(epsilon, 2)


def solve_part_2(in_data):
    oxygen = get_rating(in_data, '1', '0')
    c02 = get_rating(in_data, '0', '1')
    return int(oxygen, 2) * int(c02, 2)


def main():
    with open('in.txt') as f:
        in_data = [line.strip() for line in f]
    sol1 = solve_part_1(in_data)
    print('Part 1: {}'.format(sol1))

    sol2 = solve_part_2(in_data)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
