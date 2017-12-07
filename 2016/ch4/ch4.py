#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

from itertools import groupby

with open('input', 'r') as f:
  dis = 0

  for l in f :
    l, c = l.split("[")
    c = c.split("]")[0] 
    l = l.split("-")
    
    l, sid = "".join(l[:-1]), int(l[-1])
    
    l = sorted(l)
    
    l = [(-len(list(group)), key) for key, group in groupby(l)]
    
    l = sorted(l)[:5]
    print(l)
    
    l = "".join([c for n, c in l])
    
    print(l)
    print(c)
    
    if l == c :
      dis += sid
      
  print(dis)
  
