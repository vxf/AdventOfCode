from pprint import pprint


# seq = "211"
seq = "1321131112"


def say(s) :
  a = ""
  n = 0
  for c in s :
    if c != a:
      if n > 0 :
        yield "%d%s" % (n, a)
      a, n = c, 1
    else :
      n += 1
  yield "%d%s" % (n, a)


def recsay(s, n):
  for i in range(n):
    s = "".join([a for a in say(s)])
    
  return s


def recsay2(s, l) :
  if l == 0 :
    for c in s :
      yield c
    return
    
  a, n = "", 0
  for c in recsay2(s, l - 1) :
    if c != a:
      if n > 0 :
        yield chr(n + 48)
        yield a
      a, n = c, 1
    else :
      n += 1

  yield chr(n + 48)
  yield a


# print(len(recsay(seq, 50)))
print(len("".join(recsay2(seq, 50))))

# print(len([c for c in recsay2(seq, 50)]))
#print(sum([1 for _ in recsay2(seq, 50)]))

