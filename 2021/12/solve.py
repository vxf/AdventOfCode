INPUT_FILE = '2021/12/input.txt'

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def findpath(G, start, P, c = None):
    return sum(1 if a == 'end' else findpath(G, a, [*P, a], a if c is None and a.islower() and a in P else c) for a in filter((lambda a: a.isupper() or not a in P) if c else (lambda a: a != 'start'), G[start]))

def solve():
    i = list(l.split('-') for l in input())

    G = {}
    for s, d in i:
        if not s in G:
            G[s] = set()
        if not d in G:
            G[d] = set()

        G[d].add(s)
        G[s].add(d)

    print(findpath(G, 'start', ['start'], 'x'))
    print(findpath(G, 'start', ['start']))

solve()