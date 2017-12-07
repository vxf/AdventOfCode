#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def coordToN(x, y):
  if y < 3 :
    return str(y ** 2 + y + x - 1)
  else :
    return chr(y*2 + x - 7  + ord('A'))

def inside(x, y) :
  return x + y > 1 and x + y < 7 and abs(y-x) < 3
    

with open('input', 'r') as f:
  code = []
  n = 5
  
  x, y = 0, 2
  
  keys = {
    (2, 0) : '1',
    (1, 1) : '2',
    (2, 1) : '3',
    (3, 1) : '4',
    (0, 2) : '5',
    (1, 2) : '6',
    (2, 2) : '7',
    (3, 2) : '8',
    (4, 2) : '9',
    (1, 3) : 'A',
    (2, 3) : 'B',
    (3, 3) : 'C',
    (2, 4) : 'D'
    }
  
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
      tx, ty = vx + x, vy + y
      
      if (tx, ty) in keys :
        x, y = tx, ty
      
    code.append(keys[(x, y)])
      
  print("".join([str(n) for n in  code]))
  
with open('input', 'r') as f:
  code = []
  n = 5
  
  x, y = 0, 2
  
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
      tx, ty = vx + x, vy + y
      
      if inside(tx, ty) :
        x, y = tx, ty
      
    code.append(coordToN(x, y))
      
  print("".join([str(n) for n in  code]))

