from collections import defaultdict, Counter


def dfs(p, visited, paths, is_part2):
    if p == 'end':
        return 1
    if p.islower():
        visited[p] += 1
    t = max(visited.values()) if visited else 0
    s = 0
    for n in paths[p]:
        should_visit = visited[n] == 0 or t == 1 and is_part2 or n =='end'
        if n != 'start' and (n.islower() and should_visit or n.isupper()):
            s += dfs(n, Counter(visited), paths, is_part2)
    return s

def solve_part_1(paths):
    return dfs('start', Counter(), paths, False)

def solve_part_2(paths):
    return dfs('start', Counter(), paths, True)



def main():
    paths = defaultdict(set)
    with open('in.txt') as f:
        for line in f:
            start,end = line.strip().split('-')
            paths[start].add(end)
            paths[end].add(start)
    print(paths)
    sol1 = solve_part_1(paths)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(paths)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
