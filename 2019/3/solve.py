INPUT_FILE = 'input.txt'

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n').split(',')

def to_coords_length(l):
    x, y, s = 0, 0, 0
    for d, t in l:
        if d == 'U':
            for _ in range(t):
                y += 1
                s += 1
                yield x, y, s
        elif d == 'D':
            for _ in range(t):
                y -= 1
                s += 1
                yield x, y, s
        elif d == 'L':
            for _ in range(t):
                x -= 1
                s += 1
                yield x, y, s
        # elif d == 'R':
        else:
            for _ in range(t):
                x += 1
                s += 1
                yield x, y, s

def point_lengths(l):
    r = {}
    for x,y,s in to_coords_length(l):
        r[(x,y)] = min(r.get((x,y), s), s)
    return r

def intersect(l1, l2):
    return set((x,y) for x,y,_ in to_coords_length(l1)) & \
        set((x,y) for x,y,_ in to_coords_length(l2))

def part1(l1, l2):
    i = intersect(l1, l2)
    return min(abs(x)+abs(y) for x, y in i)

def part2(l1, l2):
    i = intersect(l1, l2)
    s1 = point_lengths(l1)
    s2 = point_lengths(l2)
    return min(s1[x,y]+s2[x,y] for x, y in i)

def solve():
    l1, l2 = [[(m[0], int(m[1:])) for m in l] for l in input()]

    print(part1(l1, l2))
    print(part2(l1, l2))

solve()