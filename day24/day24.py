from itertools import product
import sys

Z_DIV_N = []
X_ADD_N = []
Y_ADD_N = []

def execute1(model_number):
    z = 0
    for i in range(len(model_number)):
        n = int(model_number[i])
        x = ((z % 26)+ X_ADD_N[i]) != n
        z = (z // Z_DIV_N[i]) * ( 25 * x + 1) + (n + Y_ADD_N[i]) * x
    return z

def solve_part_1():
    w3, w4, w6, w7 = 1, 9, 9, 1 # Derived from input file
    for w8 in [x for x in range(9, 2, - 1)]:
        for w2, w5, w9, w14 in product([x for x in range(9, 0, -1)], repeat=4):
            for w10 in range(9, 6, -1):
                for w12 in range(9, 1, -1):
                    w11 = w10 - 6
                    w13 = w12 - 1
                    w1 = w8 - 2
                    s = f'{w1}{w2}{w3}{w4}{w5}{w6}{w7}{w8}{w9}{w10}{w11}{w12}{w13}{w14}'
                    ans = execute1(s)
                    if ans == 0:
                        return s


def solve_part_2():
    w3, w4, w6, w7 = 1, 9, 9, 1 # Derived from input file
    for w8 in [x for x in range(3, 10)]:
        for w2, w5, w9, w14 in product([x for x in range(1, 10)], repeat=4):
            for w10 in range(7, 10):
                for w12 in range(2, 10):
                    w11 = w10 - 6
                    w13 = w12 - 1
                    w1 = w8 - 2
                    s = f'{w1}{w2}{w3}{w4}{w5}{w6}{w7}{w8}{w9}{w10}{w11}{w12}{w13}{w14}'
                    ans = execute1(s)
                    if ans == 0:
                        return s


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            words = line.split()
            if words[0] == 'div' and words[1] == 'z':
                Z_DIV_N.append(int(words[2]))
            elif words[0] == 'add' and words[1] == 'x' and words[2] != 'z':
                X_ADD_N.append(int(words[2]))
            elif words[0] == 'add' and words[1] == 'y' and words[2] == 'w': 
                next_line = lines[i + 1]
                Y_ADD_N.append(int(next_line.split()[2]))
    assert len(Z_DIV_N) == len(X_ADD_N) == len(Y_ADD_N) == 14, f'lz: {len(Z_DIV_N)}, lx: {len(X_ADD_N)}, ly: {len(Y_ADD_N)}'
    sol1 = solve_part_1()
    print(f'Part 1: {sol1}')
    sol2 = solve_part_2()
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
