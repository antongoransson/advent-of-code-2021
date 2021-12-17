import sys
sys.path.append('..')
import aoc


def shoot(velocity, target, pos = (0,0)):
    dc, dr = velocity
    r, c  = pos
    c1, c2, r1, r2 = target
    max_r = r
    while r >= r1 and c <= c2:
        r += dr
        c += dc
        if dc > 0:
            dc -= 1
        elif dc < 0:
            dc += 1
        dr -= 1
        max_r = max(r, max_r)
        if r1 <= r <= r2 and c1 <= c <= c2:
            return max_r
    return None
    
def solve_part_1(c1, c2, r1 ,r2):
    ys = []
    for vc in range(c2 // 2):
        for vr in range(abs(r1)):
            result = shoot((vc, vr), (c1, c2, r1, r2))
            if result is not None:
                ys.append(result)
    return max(ys)



def solve_part_2(c1, c2, r1 ,r2):
    vs = set()
    for vc in range(c2 + 1):
        for vr in range(r1, abs(r1)):
            result = shoot((vc, vr), (c1, c2, r1, r2))
            if result is not None:
                vs.add((vc, vr))
    return len(vs)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        c1, c2, r1, r2 = aoc.get_ints(f.read())
    sol1 = solve_part_1(c1, c2, r1, r2)
    print(f'Part 1: {sol1}')
    
    sol2 = solve_part_2(c1, c2, r1 ,r2)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
