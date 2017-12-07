#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def coordToN(x, y):
  return 1 + x + y * 3

def clamp(n) :
  if n < 0 :
    return 0
  elif n > 2 :
    return 2
  else :
    return n

with open('input', 'r') as f:
  code = []
  n = 5
  
  x, y = 1, 1
  
  dirs = {
    'U' : (0,-1),
    'R' : (1, 0),
    'D' : (0, 1),
    'L' : (-1,0 )
    }

  for l in f :
    l = l.strip()
    for c in l :
      vx, vy = dirs[c]
      x, y = clamp(vx + x), clamp(vy + y)
      
    code.append(coordToN(x, y))
      
  print("".join([str(n) for n in  code]))
