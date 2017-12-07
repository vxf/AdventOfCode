#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input.txt', 'r') as f:
  data = f.read()
  
  data = [int(d) for d in data.rstrip()]
  
  print(data)
  
  a = data[-1]
  s = 0
  
  for d in data :
    if a == d :
      s += a
    a = d
    
  print(s)
