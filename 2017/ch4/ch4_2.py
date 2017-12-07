#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf
 
with open('input.txt', 'r') as f:
  c = 0
  for l in f :
    l = [sorted(w) for w in l.split()]
    
    if not any(l[i] in l[i+1:] for i in range(len(l) - 1)) :
      c += 1
      
  print(c)
        

