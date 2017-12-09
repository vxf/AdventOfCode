import string
from collections import deque

alpha = list(filter(lambda c: not c in "oil", string.ascii_lowercase))
alphalen = len(alpha)

def incChar(c) :
  return (c == alphalen - 1, (c + 1) % alphalen)

def incPass(p) :
  p = deque(p)
  n = deque()
  c = 100
  carry = True
  while carry :
    carry, c = incChar(p.pop())
    n.appendleft(c)
    # print(c)
    
  # n.extendleft(p)
  p.extend(n)
  return list(p)
  

def nextpass(p) :
  valid = False
  p = [alpha.index(c) for c in p]
  while not valid :
    p = incPass(p)
    
    validpairs = False
    pair = ()
    for w, v in zip(p, p[1:]) :
      if w == v and (w, v) != pair:
        if pair :
          validpairs = True
          break
        pair = (w, v)
     
    validseq = False
    for w, v, u in zip(p, p[1:], p[2:]) :
      w, v, u = w + 2, v + 1, u
      if w == v == u :
        validseq = True
        break
     
    # print(p)
    valid = validpairs and validseq
    
 
  p = [alpha[c] for c in p]
  return "".join(p)
  
# print(incPass([1, 2, alphalen -1]))

passwd = nextpass("vzbxkghb")
print(passwd)
passwd = nextpass(passwd)
print(passwd)
