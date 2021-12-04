import regex as re


def solve_part_1(numbers, boards):
    for n in numbers:
        for board in boards:
            for p in board:
                if n == board[p]['n']:
                    board[p]['drawn'] = True
                    bingo_c = any(all(board[r, c]['drawn'] for r in range(5)) for c in range(5))
                    bingo_r = any(all(board[r, c]['drawn'] for c in range(5)) for r in range(5))
                    if bingo_c or bingo_r:
                        s = sum(board[row]['n'] for row in board if not board[row]['drawn'])
                        return s * n


def solve_part_2(numbers, boards):
    winners = set()
    for n in numbers:
        for i, board in enumerate(boards):
            for p in board:
                if n == board[p]['n']:
                    board[p]['drawn'] = True
                    bingo_c = any(all(board[r, c]['drawn'] for r in range(5)) for c in range(5))
                    bingo_r = any(all(board[r, c]['drawn'] for c in range(5)) for r in range(5))
                    if bingo_c or bingo_r:
                        winners.add(i)
                        if len(winners) == len(boards):
                            s = sum(board[row]['n'] for row in board if not board[row]['drawn'])
                            return s * n


def main():
    with open('in.txt') as f:
        boards = []
        in_data = f.read().split('\n\n')
        numbers = list(map(int, re.findall(r'-?\d+', in_data[0])))
        for i, board in enumerate(in_data[1:]):
            boards.append({})
            for x, row in enumerate(board.split('\n')):
                for y, n in enumerate(list(map(int, re.findall(r'-?\d+', row)))):   
                    boards[i][x, y] = {'drawn': False, 'n': n}
    sol1 = solve_part_1(numbers, boards)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(numbers, boards)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
