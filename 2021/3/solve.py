INPUT_FILE = '2021/3/input.txt'

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def part1(i):
    freq = [0]*12
    t = 0

    for n in i:
        for g, b in enumerate(n):
            if b=='1':
                freq[g] += 1
        t += 1
    
    gamma = list(map(lambda g: '1' if g*2 >= t else '0', freq))
    epsilon = list(map(lambda g: '1' if g*2 <= t else '0', freq))

    print(int(''.join(gamma), 2)*int(''.join(epsilon), 2))

def oxco2(i, p):
    f = 0
    t = 0

    for n in i:
        # print(n)
        if n[p]=='1':
            f += 1
        t += 1
    
    oxigen = f*2 >= t
    co2 = f*2 < t

    return oxigen, co2

def part2(i):
    o = list(i)
    o_level = 0
    for p in range(12):
        fo = '1' if oxco2(o, p)[0] else '0'
        o = list(filter(lambda n: n[p]==fo, o))

        if len(o) == 1:
            print("O2")
            o_level = int(''.join(o[0]), 2)
            print(o_level)

    c = list(i)
    c_level = 0
    for p in range(12):
        fc = '1' if oxco2(c, p)[1] else '0'
        c = list(filter(lambda n: n[p]==fc, c))

        if len(c) == 1:
            print("CO2")
            c_level = int(''.join(c[0]), 2)
            print(c_level)

    print(o_level * c_level)

def solve():
    i = list(input())

    part1(i)
    part2(i)

solve()