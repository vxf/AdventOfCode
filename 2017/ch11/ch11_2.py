#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

import math

d = {
  'n' : (1, 0, 0),
  's' : (-1, 0, 0),
  'ne': (0, -1, 0),
  'sw': (0, 1, 0),
  'se': (0, 0, 1),
  'nw': (0, 0, -1)
}

def add(v, u) :
  x1, y1, z1 =  v
  x2, y2, z2 =  u
  
  return x1+x2, y1+y2, z1+z2
  
def merge(v) :
  done = False

  while not done :
    for i in range(3):
      j = (i+1) % 3
      a, b = v[i], v[j]
      if a*b > 0 :
        if a > 0:
          c = min(a, b)
          v = add(v, (-c, -c, -c))
        else :
          c = max(a, b)
          v = add(v, (-c, -c, -c))
        break
      done = True
      
  return v

def solve(data):
  x, y, z = 0, 0, 0
  m = 0
  
  for p in data :
    x, y, z = add(d[p], (x, y, z))
    x, y, z = merge((x, y, z,))
    m = max(m, abs(x) + abs(y) + abs(z))
    
  return m

with open('input.txt', 'r') as f:
  data = f.read()
  
  # data = "se,sw,se,sw,sw"
  
  data = [d for d in data.rstrip().split(",")]
  
  # print(data)
  
  print(solve(data))
