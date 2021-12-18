from itertools import permutations
from math import ceil
import sys
sys.path.append('..')


class Pair:

    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.is_left_child = False

    def left_is_reg(self):
        return isinstance(self.left, int)

    def right_is_reg(self):
        return isinstance(self.right, int)

    def can_explode(self):
        return self.left_is_reg() and self.right_is_reg()

    def get_pair_to_explode(self):
        if self.get_depth() >= 4 and self.can_explode:
            return self
        p = None
        if not self.left_is_reg():
            p = self.left.get_pair_to_explode()
        if not p and not self.right_is_reg():
            p = self.right.get_pair_to_explode()
        return p

    def get_left(self):
        if self.left_is_reg():
            return self
        return self.left.get_left()

    def get_right(self):
        if self.right_is_reg():
            return self
        return self.right.get_right()

    def explode_right(self):
        p = self.parent
        if self.is_left_child:
            if p.right_is_reg():
                return p
            return p.right.get_left()
        if p.is_left_child:
            if p.parent.right_is_reg():
                return p.parent
            return p.parent.right.get_left()
        p = p.parent
        while p:
            if p.is_left_child:
                break
            p = p.parent
        if p is None or p.parent is None:
            return None
        p = p.parent
        if p.right_is_reg():
            return p
        p = p.right
        return p.get_left()

    def explode_left(self):
        p = self.parent
        if not self.is_left_child:
            if p.left_is_reg():
                return p
            return p.left.get_right()
        if not p.is_left_child:
            if p.parent.left_is_reg():
                return p.parent
            return p.parent.left.get_right()
        p = p.parent
        while p:
            if not p.is_left_child:
                break
            p = p.parent
        if p is None or p.parent is None:
            return None
        p = p.parent
        if p.left_is_reg():
            return p
        p = p.left
        return p.get_right()

    def get_pair_to_split(self):
        p = None
        if self.left_is_reg():
            if self.left >= 10:
                return self
        else:
            p = self.left.get_pair_to_split()
        if p:
            return p
        if self.right_is_reg():
            if self.right >= 10:
                return self
        else:
            p = self.right.get_pair_to_split()
        return p

    def get_depth(self):
        if self.parent is None:
            return 0
        return 1 + self.parent.get_depth()

    def __str__(self):
        return f'[{self.left}, {self.right}]'

    def __add__(self, p):
        np = Pair()
        self.parent = np
        self.is_left_child = True
        p.parent = np
        np.left = self
        np.right = p
        return np

    def magnitude(self):
        ml, mr = None, None
        if self.left_is_reg():
            ml = self.left * 3
        else:
            ml = 3 * self.left.magnitude()
        if self.right_is_reg():
            mr = self.right * 2
        else:
            mr = 2 * self.right.magnitude()
        return mr + ml


def parse(line):
    i = 0
    p = Pair()
    if line[0] in '0123456789':
        return int(line[0]), 1
    while i < len(line):
        if line[i] == '[':
            i += 1
            v, j = parse(line[i:])
            p.left = v
            if isinstance(v, Pair):
                v.parent = p
                v.is_left_child = True
            i += j
        elif line[i] == ',':
            i += 1
            v, j = parse(line[i:])
            p.right = v
            if isinstance(v, Pair):
                v.parent = p
                v.is_left_child = False
            i += j
        elif line[i] == ']':
            return p, i + 1
    return p


def explode(ps):
    exp_p = ps.get_pair_to_explode()
    if not exp_p:
        return False
    parent = exp_p.parent
    lv, rv = exp_p.left, exp_p.right
    pr = exp_p.explode_right()
    pl = exp_p.explode_left()
    if pr:
        if pr.right_is_reg() and not pr.left_is_reg():
            pr.right += rv
        else:
            pr.left += rv
    if pl:
        if pl.left_is_reg() and not pl.right_is_reg():
            pl.left += lv
        else:
            pl.right += lv
    if exp_p.is_left_child:
        parent.left = 0
    else:
        parent.right = 0
    return True


def split(ps):
    p_to_split = ps.get_pair_to_split()
    if not p_to_split:
        return False
    p = Pair()
    p.parent = p_to_split
    if p_to_split.left_is_reg() and p_to_split.left >= 10:
        p.left = p_to_split.left // 2
        p.right = ceil(p_to_split.left / 2)
        p_to_split.left = p
        p.is_left_child = True
    else:
        p.left = p_to_split.right // 2
        p.right = ceil(p_to_split.right / 2)
        p_to_split.right = p
    return True


def reduce(p):
    did_explode = explode(p)
    if not did_explode:
        did_split = split(p)
    if did_explode or did_split:
        reduce(p)


def solve_part_1(lines):
    snailfishes = [parse(line)[0] for line in lines]
    sf_t = snailfishes[0]
    for sf in snailfishes[1:]:
        sf_t += sf
        reduce(sf_t)
    return sf_t.magnitude()


def solve_part_2(lines):
    s = -1
    for x, y in permutations(range(len(lines)), 2):
        xp, _ = parse(lines[x])
        yp, _ = parse(lines[y])
        p = xp + yp
        reduce(p)
        s = max(s, p.magnitude())
    return s


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    lines = []
    with open(in_f) as f:
        for line in f:
            lines.append(line.strip())
    sol1 = solve_part_1(lines)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(lines)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
