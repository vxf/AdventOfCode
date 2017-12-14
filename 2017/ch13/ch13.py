#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf


with open('input.txt', 'r') as f:
  s = 0
  
  
  for l in f :
    l, r = l.split(": ")
    l, r = int(l), int(r)
    
    if l % (2*(r-1)) == 0 :
      s += l * r
  print(s)

