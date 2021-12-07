INPUT_FILE = '2021/6/input.txt'

from collections import Counter

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def solve():
    i = map(int, next(input()).split(','))

    b, k = [0]*7, [0]*3
    for n in i:
        b[n] += 1

    # part 1
    for t in range(80):
        k[(t+2) % 3] += b[t % 7] # reproduction
        b[(t+7) % 7] += k[t % 3] # coming of age
        k[t % 3] = 0
    print(sum(b)+sum(k))

    # part 2
    for t in range(80, 256):
        k[(t+2) % 3] += b[t % 7] # reproduction
        b[(t+7) % 7] += k[t % 3] # coming of age
        k[t % 3] = 0
    print(sum(b)+sum(k))

solve()