INPUT_FILE = '2021/11/input.txt'

from itertools import product

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

ADJ = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def addvec(v, u):
    return tuple(a+b for a, b in zip(v, u))

def clip(p):
    x, y = p
    return 0 <= x < 10 and 0 <= y < 10

def adj(p):
    yield from filter(clip, (addvec(p, v) for v in ADJ))

def xyrange(w):
    yield from product(range(10), repeat=2)

def step(i):
    F = set()
    for x, y in xyrange(10):
        i[y][x] = a = i[y][x] + 1
        if a == 10:
            F.add((x, y))
    f = len(F)
    while len(F) > 0:
        G = set()
        for p in F:
            for x, y in adj(p):
                i[y][x] = a = i[y][x] + 1
                if a == 10:
                    G.add((x, y))
        F = G
        f += len(G)

    for x, y in xyrange(10):
        if i[y][x] >= 10:
            i[y][x] = 0

    return f

def solve():
    i = list(list(map(int, l)) for l in input())

    # part 1
    print(sum(step(i) for _ in range(100)))

    # part 2
    f, s = 0, 100
    while f < 100:
        f = step(i)
        s += 1
    print(s)

solve()