def get_neighbours(grid, p):
    n = set()
    for dx, dy in [(0, 1), (0, - 1), (1, 0), (-1, 0), (1, 1), (-1, - 1), (1, -1), (-1, 1)]:
        if (p[0] + dx, p[1] + dy) in grid:
            n.add((p[0] + dx, p[1] + dy))
    return n


def step(grid):
    to_flash = list()
    has_flashed = set()
    for p in grid:
        grid[p] += 1
        if grid[p] == 10:
            to_flash.append(p)
    while to_flash:
        p = to_flash.pop()
        has_flashed.add(p)
        neigbours = get_neighbours(grid, p)
        for n in neigbours:
            grid[n] += 1
            if grid[n] == 10:
                to_flash.append(n)
    for p in has_flashed:
        grid[p] = 0
    return len(has_flashed)


def solve_part_1(grid):
    s = 0
    for _ in range(100):
        n = step(grid)
        s += n
    return s


def solve_part_2(grid):
    for t in range(99999):
        n = step(grid)
        if n == len(grid):
            return t + 1


def main():
    with open('in.txt') as f:
        grid1 = {}
        grid2 = {}
        for x, line in enumerate(f):
            for y, c in enumerate(line.strip()):
                grid1[x, y] = int(c)
                grid2[x, y] = int(c)
    sol1 = solve_part_1(grid1)
    print('Part 1: {}'.format(sol1))

    sol2 = solve_part_2(grid2)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
