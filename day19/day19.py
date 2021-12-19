from collections import defaultdict
from itertools import combinations
import sys
from math import sqrt

directions = [
    lambda x, y , z: (x, y, z),
    lambda x, y , z: (x, z, y),
    lambda x, y , z: (y, x , z),
    lambda x, y , z: (y, z , x),
    lambda x, y , z: (z, y , x),
    lambda x, y , z: (z, x , y)
]

negations = [
    lambda x, y , z: ( x,  y,  z),
    lambda x, y , z: ( x, -y,  z),
    lambda x, y , z: ( x,  y, -z),
    lambda x, y , z: ( x, -y, -z),
    lambda x, y , z: (-x,  y,  z),
    lambda x, y , z: (-x, -y,  z),
    lambda x, y , z: (-x,  y, -z),
    lambda x, y , z: (-x, -y, -z)
]

def euclidean_dist(p1, p2):
    return sqrt(sum(abs(v1 - v2) ** 2 for v1, v2 in zip(p1, p2)))

def manhattan_dist(p1, p2):
    return sum(abs(v1 - v2) for v1, v2 in zip(p1, p2))

def get_dups(beacons):
    dists = {k: defaultdict(set) for k in beacons}
    for k in beacons:
        for b1, b2 in combinations(beacons[k], 2):
            d = euclidean_dist(b1, b2)
            dists[k][b1].add(d)
            dists[k][b2].add(d)
    dups = []
    for s1 in dists:
        if s1 == 0:
            continue
        for p1 in dists[0]:
            for p2 in dists[s1]:
                l = len(dists[0][p1] & dists[s1][p2])
                if l >= 11:
                    dups.append((p1, p2))
        if dups:
            return s1, dups

def get_maybe_scan_p(p1, p2, d_f, n_f):
    p2 = n_f(*d_f(*p2))
    x1, y1, z1  = p1
    x2, y2, z2  = p2
    x, y, z = x1 + x2, y1 + y2, z1 + z2
    return x, y ,z

def solve(beacons):
    scanners = [(0,0,0)]
    while len(beacons) > 1:
        s, dups = get_dups(beacons)
        found = False
        for d_f in directions:
            for n_f in negations:
                x, y, z = get_maybe_scan_p(dups[0][0], dups[0][1], d_f, n_f)
                for p1, p2 in dups:
                    if not (x, y, z) == tuple(v1 + v2 for v1, v2 in zip(p1, n_f(*d_f(*p2)))):
                        break
                else:
                    for p in beacons[s]:
                        x1, y1, z1 = n_f(*d_f(*p))
                        beacons[0].add((x - x1, y - y1, z - z1)) 
                    scanners.append((x, y, z))
                    del beacons[s]
                    found = True
                    break
            if found:
                break
    return len(beacons[0]), max(manhattan_dist(s1, s2) for s1, s2 in combinations(scanners, 2))


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    n = -1
    beacons = defaultdict(set)
    with open(in_f) as f:
        scanners = f.read().split('\n\n')
        for scanner in scanners:
            for line in scanner.split('\n'):
                if 'scanner' in line:
                    n  += 1
                else:
                    x,y,z = [int(v) for v in line.split(',')]
                    beacons[n].add((x, y , z))
    sol1, sol2 = solve(beacons)
    print(f'Part 1: {sol1}')
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
