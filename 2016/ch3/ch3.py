#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input', 'r') as f:
  i = 0

  for l in f :
    s = [int(d) for d in l.split()]
    a, b, c = sorted(s)
    
    if c < a + b :
      i += 1
      
      
  print(i)
