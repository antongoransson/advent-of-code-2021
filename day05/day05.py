from collections import Counter
import regex as re


def solve_part_1(pipes):
    return solve(pipes, True)
        
def solve(pipes, part_one):
    visited = Counter()
    for pipe in pipes:
        (x1, y1), (x2, y2) = sorted(pipe)
        if part_one and x1 != x2 and y1 != y2:
            continue
        visited[x1, y1] += 1
        while x1 != x2 or y1 != y2:
            x1 = min(x1 + 1 , x2)
            y1 = min(y1 + 1 , y2) if y1 < y2 else max(y1 - 1 , y2)
            visited[x1, y1] +=1
    return sum(v >= 2 for v in visited.values())



def solve_part_2(pipes):
    return solve(pipes, False)

def main():
    with open('in.txt') as f:
        pipes = []
        for line in f:
            x1, y1, x2, y2 = map(int, re.findall(r'-?\d+', line))
            pipes.append(((x1, y1), (x2, y2)))
    sol1 = solve_part_1(pipes)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(pipes)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
