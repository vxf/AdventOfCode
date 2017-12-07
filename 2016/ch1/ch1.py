#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input', 'r') as f:
  data = f.read()
  data = data.strip().split(', ')
  
  x, y = 0, 0
  z = 0
  
  dirs = [(0,1), (1, 0), (0, -1), (-1,0 )]
  
  for d in data :
    a, b = d[0], int(d[1:])
    
    c = -1 if a == 'L' else 1
    z = (z + c) % 4
    d = dirs[z]
    
    x, y = d[0] * b + x, d[1] * b + y
    
  print(abs(x) + abs(y))
