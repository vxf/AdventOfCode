#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input.txt', 'r') as f:

  m = [int(l.rstrip()) for l in f]
  l = len(m)
  
  pc = 0
  c = 0
  
  while pc >= 0 and pc < len(m) :
    m[pc], pc = m[pc]+1, pc+m[pc]
    c += 1
    
  print(c)

