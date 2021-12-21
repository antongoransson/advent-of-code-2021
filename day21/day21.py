from itertools import product
import sys
sys.path.append('..')
import aoc

def solve_part_1(g):
    i = 0
    rolls = 0
    while True:
        for player in sorted(g.keys()):
            i += 1
            t = i
            if i == 100:
                i = 0
            i += 2
            t += i + i -1
            rolls += 3
            p_pos = g[player]['p']
            p_pos += t
            while p_pos > 10:
                p_pos -= 10
            g[player]['s'] += p_pos
            g[player]['p'] = p_pos
            if g[player]['s'] >= 1000:
                return [g[k]['s'] * rolls for k in g if k != player][0]

def play(pos1, s1, pos2, s2, mem):
    if s1 >= 21 or s2 >= 21:
        return s1 >= 21, s2 >= 21
    if (pos1, s1, pos2, s2) in mem:
        return mem[pos1, s1, pos2, s2]
    t1, t2 = 0, 0
    for roll in product([1,2,3], [1,2,3], [1,2,3]):
            new_pos1 = pos1 + sum(roll)
            if new_pos1 > 10:
                new_pos1 -= 10
            new_s1 = s1 + new_pos1
            w2, w1 = play(pos2, s2, new_pos1, new_s1, mem)
            t1 += w1
            t2 += w2
    mem[pos1, s1, pos2, s2] = t1, t2
    return t1,t2

def solve_part_2(g):
    mem = {}
    s_p1 = g[1]['p'] 
    s_p2 = g[2]['p'] 
    return max(play(s_p1, 0, s_p2, 0, mem))

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    g = {}
    with open(in_f) as f:
        for line in f:
            player, s_pos = aoc.get_ints(line.strip())
            g[player] = {'p': s_pos, 's': 0}
    sol1 = solve_part_1({ k: dict(v) for k,v in g.items() })
    print(f'Part 1: {sol1}')
    
    sol2 = solve_part_2({ k: dict(v) for k,v in g.items() })
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
