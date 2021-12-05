INPUT_FILE = '2021/5/input.txt'

from collections import Counter

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def horver(l):
    p1, p2 = l
    return p1[0] == p2[0] or p1[1] == p2[1]

def points(i):
    for p1, p2 in i:
        x1, y1 = p1
        x2, y2 = p2
        # ver
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                yield x1, y
        # hor
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                yield x, y1
        # se
        elif x2-x1 == y2-y1:
            if x1 > x2:
                x1, x2 = x2, x1
                y1 = y2
            for a in range(x2-x1+1):
                yield x1+a, y1+a
        # ne
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1 = y2
            for a in range(x2-x1+1):
                yield x1+a, y1-a

def solve():
    i = list(tuple(tuple(map(int, p.split(','))) for p in l.split(' -> ')) for l in input())

    # part 1
    c = Counter(points(filter(horver, i)))
    print(sum(1 for p, a in c.items() if a > 1))

    # part 3
    c = Counter(points(i))
    print(sum(1 for p, a in c.items() if a > 1))

solve()