from collections import Counter
import regex as re


def solve(timers, n_days):
    current_day = Counter(t for t in timers)
    for _ in range(n_days):
        to_add = 0
        next_day = Counter()
        for k in current_day:
            prev_k = k
            k -= 1
            if k == -1:
                k = 6
                to_add += current_day[prev_k]
            next_day[k] += current_day[prev_k]
        if to_add > 0:
            next_day[8] = to_add
        current_day = next_day
    return sum(v for v in current_day.values())


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
