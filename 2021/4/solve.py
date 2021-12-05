INPUT_FILE = '2021/4/input.txt'

def input(name = INPUT_FILE):
    with open(name) as f:
        numbers = list(map(int, f.readline().strip('\n').split(',')))

        boards = []
        while f.readline():
            board = {}
            for l in range(5):
                for c, n in enumerate(map(int, f.readline().strip('\n').split())):
                    board[n] = (l, c)
            boards.append(board)

        return numbers, boards

def winners(numbers, boards):
    mark = tuple(tuple([0]*5 for _ in range(2)) for _ in boards)
    #print(mark)
    done = []
    wins = []
    for n in numbers:
        done.append(n)
        for i, b in enumerate(boards):
            if i in wins:
                continue
            if n in b:
                l, c = b[n]
                y = mark[i][0][l] + 1
                x = mark[i][1][c] + 1
                mark[i][0][l] = y
                mark[i][1][c] = x
                if x == 5 or y == 5:
                    #print('BINGO')
                    wins.append(i)
                    yield b, list(done), n

def solve():
    numbers, boards = input()

    for i, w in enumerate(winners(numbers, boards)):
        board, marked, n = w
        if i == 0:
            # part 1
            score = sum(k for k, _ in board.items() if not k in marked) * n
            print(score)

    # part 2
    score = sum(k for k, _ in board.items() if not k in marked) * n
    print(score)

solve()