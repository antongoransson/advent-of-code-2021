from operator import add, mul, gt, lt, eq
import sys


def get_f(type_id):
    if type_id == 5:
        return gt
    elif type_id == 6:
        return lt
    elif type_id == 7:
        return eq
    else:
        assert False


def read_subpacket_length(b, v, i, f, vs):
    l_sp = int(b[i: i + 15], 2)
    i += 15
    lx = 0
    while lx != l_sp:
        v_p, l_packet = read_packet(b[i:], vs)
        lx += l_packet
        i += l_packet
        v = f(v_p, v)
    return v, i


def get_value(b, i):
    n = ''
    while True:
        n += b[i + 1: i + 5]
        i += 5
        if b[i - 5] == '0':
            return int(n, 2), i


def read_n_subpackets(b, v, i, f, vs):
    ln = int(b[i: i + 11], 2)
    i += 11
    for _ in range(ln):
        v_p, l_packet = read_packet(b[i:], vs)
        i += l_packet
        v = f(v_p, v)
    return v, i


def read_packet(b, vs=[]):
    i = 0
    pv = int(b[i: i + 3], 2)
    vs.append(pv)
    type_id = int(b[i + 3:i + 6], 2)
    i += 6
    if type_id == 4:
        return get_value(b, i)
    else:
        lt_id = int(b[i], 2)
        i += 1
        if type_id in (0, 1):
            f = add if type_id == 0 else mul
            v = 0 if type_id == 0 else 1
            r_f = read_subpacket_length if lt_id == 0 else read_n_subpackets
            return r_f(b, v, i, f, vs)
        elif type_id in (2, 3):
            f = min if type_id == 2 else max
            v = 9999999999999999 if type_id == 2 else -1
            r_f = read_subpacket_length if lt_id == 0 else read_n_subpackets
            return r_f(b, v, i, f, vs)
        else:
            f = get_f(type_id)
            i += 15 if lt_id == 0 else 11
            v1, l_packet1 = read_packet(b[i:], vs)
            i += l_packet1
            v2, l_packet2 = read_packet(b[i:], vs)
            i += l_packet2
            return f(v1, v2), i


def solve_part_1(b):
    vs = []
    read_packet(b, vs)
    return sum(vs)


def solve_part_2(b):
    return read_packet(b)[0]


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = f.read().strip()
    b = (str(bin(int(in_data, 16))[2:].zfill(len(in_data) * 4)))
    sol1 = solve_part_1(b)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(b)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
