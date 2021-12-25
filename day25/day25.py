import sys


def solve_part_1(g_east, g_south, r_max, c_max):
    for t in range(1000):
        has_moved = False
        new_g_east = set()
        new_g_south = set()
        for r, c in g_east:
            new_c = (c + 1) % (c_max + 1)
            if (r, new_c) not in g_east and (r, new_c) not in g_south:
                new_g_east.add((r, new_c))
                has_moved = True
            else:
                new_g_east.add((r, c))
        for r, c in g_south:
            new_r = (r + 1) % (r_max + 1)
            if (new_r, c) not in new_g_east and (new_r, c) not in g_south:
                new_g_south.add((new_r, c))
                has_moved = True
            else:
                new_g_south.add((r, c))
        if not has_moved:
            return t + 1
        g_east = new_g_east
        g_south = new_g_south


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    g_east = set()
    g_south = set()
    r_max = -1
    c_max = -1
    with open(in_f) as f:
        for r, line in enumerate(f):
            r_max = max(r, r_max)
            for c, v in enumerate(line.strip()):
                c_max = max(c, c_max)
                if v == 'v':
                    g_south.add((r, c))
                elif v == '>':
                    g_east.add((r, c))
    sol1 = solve_part_1(g_east, g_south, r_max, c_max)
    print(f'Part 1: {sol1}')


if __name__ == "__main__":
    main()
