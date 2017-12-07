#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

from itertools import groupby

def rot(c, sid) :
  if c == ' ' :
    return c
  else :
    return chr(((ord(c) - ord('a') + sid) % 26) + ord('a'))

with open('input', 'r') as f:
  dis = 0

  for l in f :
    l, c = l.split("[")
    c = c.split("]")[0] 
    l = l.split("-")
    
    l, sid = " ".join(l[:-1]), int(l[-1])
    
    l = "".join([rot(c, sid) for c in l])
    
    if "north" in l :
    
      print(l)
      print(sid)
  
