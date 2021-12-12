from collections import defaultdict


def dfs(p, visited, paths, is_part2, t):
    if p == 'end':
        return 1
    if not t and p in visited and p.islower():
        t = True
    visited.add(p)
    s = 0
    for n in paths[p]:
        if n.isupper() or n not in visited or not t and is_part2:
            s += dfs(n, set(visited), paths, is_part2, t)
    return s

def solve_part_1(paths):
    return dfs('start', set(), paths, False, False)

def solve_part_2(paths):
    return dfs('start', set(), paths, True, False)



def main():
    paths = defaultdict(set)
    with open('in.txt') as f:
        for line in f:
            start,end = line.strip().split('-')
            if end != 'start' and start !='end':
                paths[start].add(end)
            if start != 'start' and end != 'end':
                paths[end].add(start)
            
    sol1 = solve_part_1(paths)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(paths)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
