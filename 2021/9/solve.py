INPUT_FILE = '2021/9/input.txt'

from functools import reduce
from itertools import product
from operator import mul

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def adj(x, y, w, h):
    px = x-1
    if px >= 0:
        yield px, y
    px = x+1
    if px < w:
        yield px, y
    py = y-1
    if py >= 0:
        yield x, py
    py = y+1
    if py < h:
        yield x, py

def basin(l, i):
    w , h = len(i[0]), len(i)
    V, F = set(), set((l,))
    while len(F) > 0:
        V |= F
        F = reduce(set.union, (set((q, u, v) for u, v in adj(x, y, w, h) if 9 > (q := i[v][u]) > p) for p, x, y in F)) - V

    return len(V)


def solve():
    i = tuple(tuple(map(int, l)) for l in input())

    w , h = len(i[0]), len(i)
    lows = list((p, x, y) for x, y in product(range(w), range(h)) if all(i[v][u] > (p := i[y][x]) for u, v in adj(x, y, w, h)))

    # part 1
    print(sum(d+1 for d, _, _ in lows))

    # part 2
    print(reduce(mul, sorted(basin(l, i) for l in lows)[-3:]))

solve()