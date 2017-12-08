#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def cond(r, c, v):
  if   c == '==' and r == v:
    return True
  
  elif c == '!=' and r != v:
    return True
  
  elif c == '>=' and r >= v :
    return True
  
  elif c == '<=' and r <= v :  
    return True
  
  elif c == '>' and r > v :
    return True
  
  elif c == '<' and r < v :
    return True
    
  else :
    return False


with open('input.txt', 'r') as f:
  d = {}
  n = 0
  for l in f :
    r, i, a, _, b, c, v  = l.rstrip().split()
    
    a, v = int(a), int(v)
    
    if i == 'dec' :
      a = -a 
    
    if not r in d :
      d[r] = 0
      
    if not b in d :
      d[b] = 0
      
    if cond(d[b], c, v) :
      d[r] += a
      
    if d[r] > n :
      n = d[r]
      
  # print(d)
  m = max(d.values())
  print(m)
  print(n)


  
