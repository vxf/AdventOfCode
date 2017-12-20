#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

import operator
from functools import reduce

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
def khash(data):
  # data = f.read().rstrip()
  
  m = [n for n in range(256)]
  
  # data = "AoC 2017"
  data = [ord(c) for c in data] + [17, 31, 73, 47, 23]
  # print(data)
  
  a = len(m)
  
  p = 0
  s = 0
  
  for _ in range(64) :
  
    for l in data :
      e = p+l
      
      if p+l < a :
        r = m[p:e]
        r = r[::-1]
        
        m = m[:p] + r + m[e:]
      else :
        r = m[p:] + m[:e-a]
        r = r[::-1]
        
        m = r[a-p:] + m[e-a:p] + r[:a-p]
        
      p = (p+l+s) % a
      s += 1
      
  m = [reduce(operator.xor, c) for c in chunks(m, 16)]
  
  return m
  
def digest(h):
  return "".join(["{0:02x}".format(c) for c in h])

# data = "AoC 2017"
data = "ljoxqyyw"

#h = khash(data)

#print("{0:b}".format(h[0]))

#print(digest(h))


t = sum(sum(sum(1 if b == "1" else 0 for b in "{0:b}".format(c)) for c in khash("%s-%d" % (data, s))) for s in range(128))
print(t)
