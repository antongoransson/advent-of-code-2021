import sys
sys.path.append('..')
import aoc


def fold(f, grid):
    c, n = f
    new_grid = {}
    for p in grid.keys():
        y, x = p
        if c == 'y' and y > n:
            y = 2 * n - y
        elif c == 'x' and x > n:
            x = 2 * n - x
        new_grid[(y, x)] = True
    return new_grid


def solve_part_1(grid, folds):
    return len(fold(folds[0], grid))


def solve_part_2(grid, folds):
    for f in folds:
        grid = fold(f, grid)
    return aoc.get_s_grid(grid)


def main():
    grid = {}
    folds = []
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
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
                    grid[y, x] = True
    sol1 = solve_part_1(grid, folds)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid, folds)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
