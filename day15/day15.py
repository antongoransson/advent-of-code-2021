from heapq import heappush, heappop
import sys
sys.path.append('..')
import aoc

def expand(grid):
    new_grid = {}
    lr, lc = max(r for r, c in grid) + 1, max(c for r, c in grid) + 1
    for p in grid:
        r, c = p
        for rr in range(0, 5):
            for cc in range(0, 5):
                n_r = grid[r, c] + rr + cc
                n_r = n_r if n_r <= 9 else (n_r) % 10 + 1
                new_grid[r + rr * lr, c + cc * lc] = n_r
    return new_grid

def dijkstra(grid, start, goal):
    pq = [(0, start)]
    costs = {}
    while pq:
        risk, p = heappop(pq)
        if p == goal:
            return risk
        for n_p in aoc.neighbours(grid, p):
            n_c = risk + grid[n_p]
            if n_p not in costs or n_c < costs[n_p]:
                costs[n_p] = n_c
                heappush(pq, (n_c, n_p))


def solve_part_1(grid):
    goal = (max(r for r, c in grid), max(c for r, c in grid))
    return dijkstra(grid, (0, 0), goal)

def solve_part_2(grid):
    expanded_g = expand(grid)
    lr, lc = max(r for r, c in expanded_g), max(c for r, c in expanded_g)
    goal = (lr, lc)
    return dijkstra(expanded_g, (0, 0), goal)


def main():
    grid = {}
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        for r, line in enumerate(f):
            for c, n in enumerate(line.strip()):
                grid[r, c] = int(n)
    sol1 = solve_part_1(grid)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
