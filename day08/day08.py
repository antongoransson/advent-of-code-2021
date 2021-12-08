def sorted_s(s):
    return ''.join(sorted(s))

def get_signal(o, f):
   a, = [x for x in o if f(x)]
   return  sorted_s(a)


def solve_part_1(out_signals):
    return sum(len(x) in (2, 3, 4 ,7) for o in out_signals for x in o)

def solve_part_2(in_signals, out_signals):
    s = 0
    for in_s, out_s in zip(in_signals, out_signals):
        n1 = get_signal(in_s, lambda x:  len(x) == 2)
        n4 = get_signal(in_s, lambda x:  len(x) == 4)
        n7 = get_signal(in_s, lambda x:  len(x) == 3)
        n8 = get_signal(in_s, lambda x:  len(x) == 7)
        n3 = get_signal(in_s, lambda x: len(x) == 5 and len(set(n7) & set(x)) == 3)

        top_mid_s, = [c for c in n7 if c not in n1]
        mid_s, = [c for c in n3 if c in n4 and c not in n1]
        bottom_s, = [c for c in n3 if c not in n4 and c not in n7]
        top_left_s, = [c for c in n4 if c != mid_s and c not in n7]

        n5 = get_signal(in_s, lambda x: len(x) == 5 and len(set([top_mid_s, top_left_s, mid_s, bottom_s]) & set(x)) == 4)

        top_righs_s, = [c for c in n5 if c not in [top_mid_s, top_left_s, mid_s, bottom_s]]
        b_right_s, = [c for c in n1 if c != top_righs_s]

        n2 = get_signal(in_s, lambda x: len(x) == 5 and sorted_s(x) != n3 and sorted_s(x) != n5)
        n6 = get_signal(in_s, lambda x: len(x) == 6 and b_right_s not in x)
        n0 = get_signal(in_s, lambda x: len(x) == 6 and mid_s not in x)
        n9 = get_signal(in_s, lambda x: len(x) == 6 and sorted_s(x) != n6 and sorted_s(x) != n0)

        mapping = {n: str(i) for i, n in enumerate((n0, n1, n2, n3, n4,n5 ,n6 ,n7, n8, n9))}
        s += int(''.join([mapping[sorted_s(n)] for n in out_s]))
    return s


def main():
    with open('in.txt') as f:
        in_signals = []
        out_signals = []
        for line in f:
            i,o = line.strip().split('|')
            in_signals.append(i.split())
            out_signals.append(o.split())
    sol1 = solve_part_1(out_signals)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(in_signals, out_signals)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
