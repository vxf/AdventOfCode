#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

"""
with open('input.txt', 'r') as f:
  d = {}
  for l in f :
    l = l.split()
    s = "".join(l[3:])
    
    if s == '' : continue
    
    if not l[0] in d :
        d[l[0]] = True
    
    s = s.split(",")

    for c in s:
      d[c] = False
   
  print(next(key for key, value in d.items() if value))"""

with open('input.txt', 'r') as f:
  candidates = set()
  children = set()
  
  for l in f :
    l = l.split()
    s = "".join(l[3:])
    
    if s == '' : continue

    candidates.add(l[0])
    
    children |= set(s.split(","))
   
  print((candidates - children).pop())

