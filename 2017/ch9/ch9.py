#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

with open('input.txt', 'r') as f:
  data = f.read()
  
  data = data.rstrip()
  
  s = 0
  
  # data = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
  
  l = 0
  g = False
  h = False
  gc = 0
  
  for c in data :
    if h :
      h = False
      
    elif g :
      if c == '>' :
        g = False
      elif c == '!' :
        h = True
      else :
        gc += 1
        
    else:
      if c == '{' :
        l += 1
        s += l
      elif c == '}' :
        l -= 1
      if c == '<' :
        g = True
  
  # print(data)
  print(s)
  print(gc)
