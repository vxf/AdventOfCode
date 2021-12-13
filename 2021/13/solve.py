INPUT_FILE = '2021/13/input.txt'

def input(name = INPUT_FILE):
    points = []
    folds = []
    skip = len('fold along ')
    with open(name) as f:
        for l in f:
            l = l.strip('\n')
            if not l :
                break
            x, y = l.split(',')
            points.append((int(x), int(y)))

        for l in f:
            l = l[skip:].strip('\n')
            folds.append(fold(l[0], int(l[2:])))

    return points, folds
        
def fold(a, b):
    return (lambda x, y: (-(abs(-x+b)-b), y)) if a == 'x' else (lambda x, y: (x, -(abs(-y+b)-b)))

def display(points):
    xmin = min(x for x,_ in points)
    ymin = min(y for _,y in points)
    xmax = max(x for x,_ in points)-xmin+1
    ymax = max(y for _,y in points)-ymin+1

    screen = [['.']*xmax for _ in range(ymax)]
    for x, y in points:
        screen[y-ymin][x-xmin] = '#'
    for l in screen:
        print(''.join(l))

def solve():
    points, folds = input()

    # Part 1
    f = folds[0]
    print(len({f(*p) for p in points}))

    # Part 2
    q = set(points)
    for f in folds:
        q = {f(*p) for p in q}
    display(q)

solve()