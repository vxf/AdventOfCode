#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def visit(n, d, v):
  v[n] = 1
  for c in d[n] :
    if v[c] == 0 :
      visit(c, d, v)

with open('input.txt', 'r') as f:
  d = []

  for l in f :
    # print(l)
    _, c = l.split(" <-> ")
    # a = int(a)
    c = [int(x) for x in c.split(", ")]
    
    d.append(c)
    
  v = [0]*len(d)
  
  visit(0, d, v)

  # print(d)
  
  print(sum(v))

