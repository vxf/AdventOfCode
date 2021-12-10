INPUT_FILE = '2021/10/input.txt'

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

SCORE = (
    ('(', ')', 3, 1),
    ('[', ']', 57, 2),
    ('{', '}', 1197, 3),
    ('<', '>', 25137, 4)
)

def solve():
    i = input()

    openchr = set(a for a,_,_,_ in SCORE)
    corrscr = {b: (a, c) for a,b,c,_ in SCORE}
    incmscr = {a: d for a,_,_,d in SCORE}

    t = 0
    scomp = []
    for l in i:
        S = []
        for c in l:
            if c in openchr:
                S.append(c)
            else:
                e, s = corrscr[c]
                if e != S.pop():
                    t += s
                    S = []
                    break
        if len(S) > 0:
            scomp.append(sum(incmscr[c]*5**e for e, c in enumerate(S)))

    # part 1
    print(t)

    # part 2
    print(sorted(scomp)[int(len(scomp)/2)])

solve()