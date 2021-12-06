from collections import Counter
import regex as re


def solve(timers, n_days):
    current_day = Counter(timers)
    for _ in range(n_days):
        next_day = Counter()
        for k, v in current_day.items():
            k -= 1
            if k == -1:
                k = 6
                next_day[8] += v
            next_day[k] += v
        current_day = next_day
    return sum(current_day.values())


def solve_part_1(timers):
    return solve(timers, 80)


def solve_part_2(timers):
    return solve(timers, 256)


def main():
    with open('in.txt') as f:
        timers = list(map(int, re.findall(r'-?\d+', f.read())))
    sol1 = solve_part_1(timers)
    print('Part 1: {}'.format(sol1))

    sol2 = solve_part_2(timers)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
