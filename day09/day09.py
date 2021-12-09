from functools import reduce
from operator import mul


def get_neighbours(grid, p):
    neigbours = list()
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        neigbour = (p[0] + dx, p[1] + dy)
        if neigbour in grid:
            neigbours.append(neigbour)
    return neigbours

def solve_part_1(grid):
    return sum(grid[p] + 1 for p in grid if all(grid[p] < grid[n] for n in get_neighbours(grid, p)))

def solve_part_2(grid):
    low_points = [p for p in grid if (all(grid[p] < grid[n] for n in get_neighbours(grid, p)))]
    basins = []
    for lp in low_points:
        basin = [lp]
        visited = set(lp)
        to_visit = [(lp, get_neighbours(grid, lp))]
        while to_visit:
            p, neighbours = to_visit.pop() 
            for n in neighbours:
                if grid[n] != 9 and grid[n] > grid[p] and n not in visited:
                    visited.add(n)
                    basin.append(n)
                    to_visit.append((n, get_neighbours(grid, n)))
        basins.append(basin)
    basins.sort(key=len, reverse=True)
    return reduce(mul, [len(b) for b in basins[:3]])


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
