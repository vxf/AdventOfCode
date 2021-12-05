INPUT_FILE = '2021/2/input.txt'

from functools import reduce
from operator import add

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

CMDS1 = {
    'forward': lambda x: (x, 0),
    'up': lambda x: (0, -x),
    'down': lambda x: (0, x),
}

CMDS2 = {
    'forward': lambda a, x: (x, a*x, 0),
    'up': lambda _, x: (0, 0, -x),
    'down': lambda _, x: (0, 0, x),
}

def addv(a, b):
    return tuple(map(add, a , b))

def part1(i):
    x, y = reduce(
        addv,
        map(lambda c: CMDS1[c[0]](int(c[1])), i),
        (0, 0)
    )
    print(x*y)

def step(s, c):
    c, t = c
    _, _, a = s
    return addv(s, c(a, t))

def part2(i):
    x, y, _ = reduce(
        step,
        map(lambda c: (CMDS2[c[0]], int(c[1])), i),
        (0, 0, 0)
    )
    print(x*y)

def solve():
    i = list(map(str.split, input()))
    part1(i)
    part2(i)

solve()