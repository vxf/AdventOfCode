#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

import csv

with open('input.txt', 'r') as f:
  rd = csv.reader(f, delimiter='\t')
  
  s = 0
  
  for r in rd :
    r = sorted((int(c) for c in r), reverse=True)
    
    for i in range(len(r) - 1) :
      a = r[i]
      for b in r[i+1:]:
        if a % b == 0 :
          s += a // b
    
  print(s)
