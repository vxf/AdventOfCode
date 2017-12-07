#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def getABAs(s) :
  if len(s) < 3 :
    return []
  abas = []
    
  for a, b, c in zip(s[:-2], s[1:-1], s[2:]) :
    if a == c and a != b :
      abas.append(a+b)
      
  return abas

def isTTL(l) :
  bab = []
  aba = []

  for p in (']'+l).split('[') :
    b, a = p.split(']')
    
    bab = bab + [d+c for c, d in getABAs(b)]
    aba = aba + getABAs(a)
  
  return any(a in bab for a in aba)

with open('input', 'r') as f:
  i = 0

  for l in f :
    l = l.strip()
    if isTTL(l) :
      i += 1
      
  print(i)
    
