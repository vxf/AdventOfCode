INPUT_FILE = 'input.txt'

from itertools import tee

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

def solve():
    i = list(map(int, input()))

    # Part 1
    r = sum(map(lambda a: a[0] < a[1], tuplewise(i)))
    print(r)

    # Part 2
    r = sum(map(lambda a: a[0] < a[1], tuplewise(map(sum, tuplewise(i, 3)))))
    print(r)

solve()