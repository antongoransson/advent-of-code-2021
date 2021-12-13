from operator import mul
from functools import reduce
import sys
sys.path.append('..')
import aoc

def solve_part_1(grid):
    return sum(grid[p] + 1 for p in grid if all(grid[p] < grid[n] for n in aoc.neighbours(grid, p)))


def solve_part_2(grid):
    low_points = [p for p in grid if (
        all(grid[p] < grid[n] for n in aoc.neighbours(grid, p)))]
    basins = []
    for lp in low_points:
        visited = set([lp])
        to_visit = [(lp, aoc.neighbours(grid, lp))]
        while to_visit:
            p, neighbours = to_visit.pop()
            for n in neighbours:
                if grid[n] != 9 and grid[n] > grid[p] and n not in visited:
                    visited.add(n)
                    to_visit.append((n, aoc.neighbours(grid, n)))
        basins.append(len(visited))
    return reduce(mul, sorted(basins, reverse=True)[:3])


def main():
    grid = {}
    with open('in.txt') as f:
        for x, line in enumerate(f):
            for y in range(len(line.strip())):
                grid[x, y] = int(line[y])
    sol1 = solve_part_1(grid)
    print('Part 1: {}'.format(sol1))

    sol2 = solve_part_2(grid)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
