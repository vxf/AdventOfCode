INPUT_FILE = '2021/8/input.txt'

from collections import Counter

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

CRIB = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]

def learn(crib):
    found = [1, 4, 7, 8]
    decisions = []

    c = [d for i, d in enumerate(crib) if not i in found]
    while len(c) > 0:
        for s in found:
            # get intersections sizes with s
            t = crib[s]
            intsizes = {d: sum(u in d for u in t) for d in c}
            # find the unique intersection size
            d, f = Counter(i for _, i in intsizes.items()).most_common()[-1]
            if f == 1:
                # find the number
                i = crib.index(next(j for j, i in intsizes.items() if i == d))
                found.append(i)
                decisions.append((s, d, i))
                break
        c = [d for i, d in enumerate(crib) if not i in found]

    # print(decisions)

    return decisions

def guess(patterns, lengths, decisions):
    r = [None,]*10
    match = {}
    for a in patterns:
        a = ''.join(sorted(a))
        x = len(a)
        match[a] = tuple(z for z, y in enumerate(lengths) if x == y)

    for k, v in list(match.items()):
        if len(v) == 1:
            r[v[0]] = k
            del match[k]

    for known, s, found in decisions:
        k = next(k for k, _ in match.items() if s == sum(j in k for j in r[known]))
        r[found] = k
        del match[k]

    return r

def calcvalue(cypher, value):
    return sum(cypher.index(''.join(v))*(10**e) for e, v in enumerate(reversed(value)))

def solve():
    i = tuple(tuple(tuple(map(sorted, j.split())) for j in l.rsplit(' | ')) for l in input())

    lengths = tuple(len(n) for n in CRIB)

    # part1
    s = tuple(lengths[n] for n in (1, 4, 7, 8))
    print(sum(sum(len(d) in s for d in o) for _, o in i))

    # part 2
    decisions = learn(CRIB)
    print(sum(calcvalue(guess(p, lengths, decisions), v) for p, v in i))

solve()