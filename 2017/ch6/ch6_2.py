#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

inputs = [
            [0,2,7,0],
            [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11],
            [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
         ]

def maxp(m):
  j = 0
  n = -1
  for i in range(len(m)):
    if m[i] > n :
      j, n = i, m[i]
      
  return j, n

def dist(m):
  l = len(m)
  p, n = maxp(m)
  
  a, b = n // l, n % l
  
  m2 = [c+a for c in m]
  m2[p] = a
  
  for i in range(b):
    m2[(p+1+i) % l] += 1
  
  return m2

def run(m):
  s = [m,]
  c = 0
  
  while True :
    n = dist(m)
    c += 1
    
    try:
      i = s.index(n)
      return c - i
    except ValueError as e:
      pass
    m = n
    s.append(n)
    
  return c

"""
with open('input.txt', 'r') as f:
  m = [int(b) for b in f.read().rstrip().split('\t')]
  # print(m)
  
  print(run(m))"""
  
for puzzle in inputs:
    print(puzzle, run(puzzle))
