#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input.txt', 'r') as f:
  d = {}
  for l in f :
    l = l.split()
    s = "".join(l[3:])
    
    if s == '' : continue
    
    if not l[0] in d :
        d[l[0]] = 0
    
    s = s.split(",")

    for c in s:
      if c in d :
        d[c] += 1
      else :
        d[c] = 1
   
  print(next(key for key, value in d.items() if value == 0))

