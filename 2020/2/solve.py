INPUT_FILE = '2020/2/input.txt'

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def solve():
    valid = 0
    valid2 = 0
    for l in input():
        r,s,p = l.split()
        r1,r2=r.split('-')
        r1,r2=int(r1),int(r2)
        s = s[0]

        n = p.count(s)
        if n >= r1 and n <= r2:
            valid+=1

        if (p[r1-1] == s) != (p[r2-1] == s):
            valid2 += 1

    print(valid)
    print(valid2)

solve()