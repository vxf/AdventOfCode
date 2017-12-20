#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input.txt', 'r') as f:
  data = f.read()
  
  data = data.split(",")
  
  # print(data)
  
  p = [x for x in range(16)]
  
  for o in data :
    base = ord("a")
    
    if o[0] == "s" :
      n = int(o[1:])
      p = p[-n:] + p[:-n]
      
    elif o[0] == "x" :
      a, b = o[1:].split("/")
      a, b = int(a), int(b)
      p[a], p[b] = p[b], p[a]
    
    else : #  o[0] == "p" :
      a, b = o[1:].split("/")
      a, b = p.index(ord(a)-base), p.index(ord(b)-base)
      p[a], p[b] = p[b], p[a]
      
  
  p = [chr(ord("a")+x) for x in p]
  
  print("".join(p))
