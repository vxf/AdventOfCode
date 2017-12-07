#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input', 'r') as f:
  data = f.read()
  data = data.strip().split(', ')
  
  locs = [(0, 0)]
  
  x, y = 0, 0
  z = 0
  breaker = 0
  
  dirs = [(0,1), (1, 0), (0, -1), (-1,0 )]
  
  for d in data :
    a, b = d[0], int(d[1:])
    
    c = -1 if a == 'L' else 1
    z = (z + c) % 4
    d = dirs[z]
    
    # x, y = d[0] * b + x, d[1] * b + y
    
    for n in range(b) :
      x, y = d[0] + x, d[1] + y
    
      if (x, y) in locs :
        breaker = 1
        break
      
      locs.append((x, y))
      
    if breaker : break
  
  print(abs(x) + abs(y))
