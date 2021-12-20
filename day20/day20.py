import sys


def print_grid(grid):
    min_r, min_c = min(r for r, c in grid), min(c for r, c in grid)
    max_r, max_c = max(r for r, c in grid), max(c for r, c in grid)
    s = ''
    for rr in range(min_r - 1, max_r + 2):
        for cc in range(min_c - 1, max_c + 2):
            s += grid[rr, cc] if (rr, cc) in grid else 'x'
        s += '\n'
    print(s)


def get_bin(grid, r, c, pad_c):
    s = ''
    for rr in range(r - 1, r + 2):
        for cc in range(c - 1, c + 2):
            grid_c = grid[rr, cc] if (rr, cc) in grid else pad_c
            s += '1' if grid_c is '#' else '0'
    return int(s, 2)

def solve(alg, grid, t):
    pad_c_odd_t = alg[0]
    s = ''.join('1' if v == '#' else '0' for v in pad_c_odd_t * 9)
    pad_c_even_t = alg[int(s, 2)]
    min_r, min_c = min(r for r, c in grid), min(c for r, c in grid)
    max_r, max_c = max(r for r, c in grid), max(c for r, c in grid)
    for i in range(t):
        pad_c = pad_c_even_t if i % 2 == 0 else pad_c_odd_t
        new_grid = {}
        for r in range(min_r - 1, max_r + 2):
            for c in range(min_c - 1, max_c + 2):
                b = get_bin(grid, r, c, pad_c)
                new_grid[r, c] = alg[b]
        min_r -= 1
        min_c -= 1
        max_c += 1
        max_r += 1
        grid = new_grid
    return new_grid


def solve_part_1(alg, grid):
    grid = solve(alg, grid, 2)
    return sum(1 for v in grid.values() if v is '#')


def solve_part_2(alg, grid):
    grid = solve(alg, grid, 50)
    return sum(1 for v in grid.values() if v is '#')


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    grid = {}
    with open(in_f) as f:
        alg, image = f.read().split('\n\n')
        for i, r in enumerate(image.split()):
            for j, c in enumerate(r):
                grid[i, j] = c
    sol1 = solve_part_1(alg, grid)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(alg, grid)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
