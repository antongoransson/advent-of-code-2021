def fold(f, grid):
    c, n = f
    new_grid = {}
    for p in grid.keys():
        y, x = p
        if c == 'y' and y > n:
            y = 2 * n - y
        elif c == 'x' and x > n:
            x = 2 * n - x
        new_grid[(y, x)] = 1
    return new_grid


def solve_part_1(grid, folds):
    return len(fold(folds[0], grid))


def solve_part_2(grid, folds):
    for f in folds:
        grid = fold(f, grid)
    x = max(p[1] for p in grid)
    y = max(p[0] for p in grid)
    s = '\n'
    for y in range(y + 1):
        for x in range(x + 1):
            if (y, x) in grid and grid[y, x]:
                s += '#'
            else:
                s += '.'
        s += '\n'
    return s


def main():
    grid = {}
    folds = []
    with open('in.txt') as f:
        for line in f:
            if 'fold' in line:
                n = int(line.split('=')[1])
                if 'x' in line:
                    folds.append(('x', n))
                else:
                    folds.append(('y', n))
            else:
                if line.strip():
                    x, y = map(int, line.strip().split(','))
                    grid[y, x] = 1
    sol1 = solve_part_1(grid, folds)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid, folds)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
