import regex as re

def get_s_grid(grid, in_grid_c = '#', o_grid_c = ' '):
    min_x = min(x for x, y in grid)
    max_x = max(x for x, y in grid)
    min_y = min(y for x, y in grid)
    max_y = max(y for x, y in grid)
    s = '\n'
    for x in range(max_x - min_x + 1):
        for y in range(max_y - min_y + 1):
            s += in_grid_c if (x, y) in grid and grid[x, y] else o_grid_c
        s += '\n'
    return s

def neighbours(grid, p, diag=False):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if diag:
        deltas += [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    x, y = p
    neigbours = set()
    for dx, dy in deltas:
        xx = x + dx
        yy = y + dy
        if (xx, yy) in grid:
            neigbours.add((xx, yy))
    return neigbours


def get_ints(s, sign=True):
    if sign:
        return list(map(int, re.findall(r'-?\d+', s)))
    else:
        return list(map(int, re.findall(r'\d+', s)))