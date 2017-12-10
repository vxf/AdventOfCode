#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input.txt', 'r') as f:
  data = f.read()
  
  data = [int(d) for d in data.split(",")]
  
  m = [n for n in range(256)]
  
  #data = [3, 4, 1, 5]
  #m = [n for n in range(5)]
  
  a = len(m)
  
  p = 0
  s = 0
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
    
  print(m[0]*m[1])
