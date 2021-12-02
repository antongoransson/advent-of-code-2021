def solve_part_1(in_data):
    x, y = 0, 0
    for c, v in in_data:
        v = int(v)
        if c == 'forward':
            x += v
        elif c == 'up':
            y -= v
        elif c == 'down':
            y += v
    return y*x


def solve_part_2(in_data):
    x, y, aim = 0, 0, 0
    for c, v in in_data:
        v = int(v)
        if c == 'forward':
            x += v
            y += aim * v
        elif c == 'up':
            aim -= v
        elif c == 'down':
            aim += v
    return x * y


def main():
    with open('in.txt') as f:
        in_data = [line.strip().split() for line in f]
    sol1 = solve_part_1(in_data)
    print('Part 1: {}'.format(sol1))

    sol2 = solve_part_2(in_data)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
