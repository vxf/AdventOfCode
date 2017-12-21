#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

# s = 3
s = 312 # puzzle input

b = [0, ]
p = 0
n = 50000000 # n insertions

last = 0

for x in range(1, n+1) :
  # print(p)
  p = (p + s) % x
  p += 1
  if p == 1 :
    last = x
    
print(last)
