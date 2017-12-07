#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

import csv

with open('input.txt', 'r') as f:
  rd = csv.reader(f, delimiter='\t')
  
  s = 0
  
  for r in rd :
    r = [int(c) for c in r]
    s += max(r) - min(r)
    
  print(s)
