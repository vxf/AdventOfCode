#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

# s = 3
s = 312 # puzzle input

b = [0, ]
p = 0
n = 2017 # n insertions

for x in range(1, n+1) :
  # print(p)
  p = (p + s) % len(b)
  p += 1
  b.insert(p, x)
  
print(b[p-3:p+4])
