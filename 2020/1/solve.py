INPUT_FILE = 'input.txt'

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def part1(l):
    for x in l:
        l.pop()
        for y in l:
            if x+y == 2020:
                return x*y

def part2(l):
    for x in l:
        l.pop()
        m = list(l)
        for y in m:
            m.pop()
            for z in m:
                if x+y+z == 2020:
                    return x*y*z

def solve():
    l = sorted(int(n) for n in input())

    print(part1(l))
    print(part2(l))

solve()