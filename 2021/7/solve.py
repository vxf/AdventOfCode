INPUT_FILE = '2021/7/input.txt'

from collections import Counter

def input(name = INPUT_FILE):
    with open(name) as f:
        for l in f:
            yield l.strip('\n')

def solve():
    i = map(int, next(input()).split(','))

    i = sorted(i)
    l = len(i)/2
    m = i[int(l)]

    # part 1
    # https://en.wikipedia.org/wiki/Geometric_median#Properties
    # https://en.wikipedia.org/wiki/Median
    print(sum(abs(x - m) for x in i))

    # part 2
    # the average provides an accurate enough approximation but why????
    # y = int(sum(i)/len(i))
    # print(int(sum((n := abs(x - y))*(n+1)/2 for x in i)))
    print(int(min(sum((n := abs(x - y))*(n+1)/2 for x in i) for y in range(i[0], i[-1]))))

solve()