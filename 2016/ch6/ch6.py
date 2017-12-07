#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

import itertools

def mostFreq(f):
  c, g = max(itertools.groupby(sorted(f)),
    key = lambda g: len(list(g[1])))
  #print(c)
  
  return c

with open('input', 'r') as f:
  freqs = [[], [], [], [], [], [], [], []]

  for l in f :
    l = l.strip()
    
    for c, f in zip(l, freqs) :
      f.append(c)
  
  freqs = [mostFreq(f) for f in freqs]
  
  print(''.join(freqs))
