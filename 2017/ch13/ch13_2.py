#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def good(fw, d) :
  for l, r in fw :
    
    if (l+d) % (2*(r-1)) == 0 :
      return False
  return True

with open('input.txt', 'r') as f:
  s = 0
  
  fw = []
  
  for l in f :
    l, r = l.split(": ")
    l, r = int(l), int(r)
    
    fw.append((l, r,))
  
  d = 0
  
  while not good(fw, d) :
    d += 1
       
  print(d)

