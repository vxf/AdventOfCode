INPUT_FILE = '2021/14/input.txt'

from itertools import tee
from collections import Counter

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def tuplewise(iterable, n=2):
    # extending pairwise to n tuple
    # https://docs.python.org/3/library/itertools.html#itertools.pairwise
    iters = tee(iterable, n)
    for i, iter in enumerate(iters):
        for _ in range(i):
            next(iter, None)
    return zip(*iters)

def insert(p, n, tr, c=1):
    if not p in tr:
        tr[p] = Counter()
    tr[p][n] += c

def step(rules, tr):
    tr2 = {}
    for a, c in tr.items():
        for b, n in c.items():
            i = rules.get((a, b), None)
            if i is None:
                insert(a, b, tr2, n)
            else:
                insert(a, i, tr2, n)
                insert(i, b, tr2, n)
    return tr2

def score(start, tr):
    counts = sum((c for _, c in tr.items()), Counter())
    counts[start] += 1
    mc = counts.most_common()

    return mc[0][1] - mc[-2][1]

def solve():
    i = list(input())

    template = i[0]
    rules = {(r[0], r[1]): r[6] for r in i[2:]}
    tr = {}
    for a, b in tuplewise(template):
        insert(a, b, tr)
    insert(template[-1], 'e', tr)

    # part 1
    for _ in range(10):
        tr = step(rules, tr)
    print(score(template[0], tr))

    # part 2
    for _ in range(30):
        tr = step(rules, tr)
    print(score(template[0], tr))

solve()