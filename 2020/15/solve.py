INPUT = [1,12,0,20,8,16]

def calc(d, n, start, end):
    for i in range(start, end-1):
        a = i - d.get(n, i)
        d[n] = i
        n = a
    return n

def solve():
    d = {n: i for i, n in enumerate(INPUT[:-1])}
    n = INPUT[-1]

    n = calc(d, n, len(d), 2020)
    print(n)

    n = calc(d, n, 2020, 30000000)
    print(n)

solve()