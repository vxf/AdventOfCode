#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def hasABBA(s) :
  if len(s) < 4 :
    return False

  for a, b, c, d in zip(s[:-3], s[1:-2], s[2:-1], s[3:]) :
    if a == d and b == c and a != b :
      return True
      
  return False

def isTTL(l) :
  abba = False

  for p in (']'+l).split('[') :
    b, a = p.split(']')
    
    if hasABBA(b) :
      return False
      
    abba = abba or hasABBA(a)
    
  return abba

with open('input', 'r') as f:
  i = 0

  for l in f :
    l = l.strip()
    if isTTL(l) :
      i += 1
      
  print(i)
    
