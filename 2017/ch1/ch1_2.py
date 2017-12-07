#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input.txt', 'r') as f:
  data = f.read()
  
  data = [int(d) for d in data.rstrip()]
  
  # print(data)
  
  l = len(data)
  o = l // 2
  
  a = data[-1]
  s = 0
  
  for d in range(l) :
    if data[d] == data[(o + d) % l] :
      s += data[d]
    
  print(s)
