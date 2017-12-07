#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def getTris(f) :
  l3 = [None]*3
  ln = 0
  for l in f :
    l3[ln % 3] = [int(d) for d in l.split()]
    ln += 1
    
    if ln % 3 == 0 :
      yield (l3[0][0], l3[1][0], l3[2][0])
      yield (l3[0][1], l3[1][1], l3[2][1])
      yield (l3[0][2], l3[1][2], l3[2][2])

with open('input', 'r') as f:
  i = 0

  for t in getTris(f) :
    a, b, c = sorted(t)
    
    if c < a + b :
      i += 1
      
      
  print(i)
