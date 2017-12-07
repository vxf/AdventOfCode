#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

n = 368078
# n = 1024
# n = 12
# n = 23

def odds():
  x = 0
  while True :
    yield x, 2*x + 1
    x += 1

a = 0
b = 0
c = 0
for i, x in odds():
  c = x
  if x*x > n :
    break
  b = i
  a = x
 
#print(a)
#print(b)
#print(c)
# print(((n - a*a) % ((c*c - a*a) // 4)) )
# print(c*c - a*a)

m = 2 * (b + 1)
#print(b)

print(b + 1 + abs((n - (a*a)) % m - (b+1)))
