#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

n = 368078
# n = 1024
# n = 12
# n = 23


# s = [1, 1, 2, 4, 5, 10, 11, 23, 25]
s = [1, 1, 1, 1, 1, 1, 1, 1, 1] # start array with the 1 propagated

def run(n):
  CORNER = 1
  PRECORNER = 2

  i = 1 # current index to propagate
  b = 1 # current radius

  while True :
    m = 2 * b # size of the square side at this radius
    
    s.extend([0]*((2 * (b+1))*4)) # expand spiral array at 0
    
    # pointer to the start of the affected range
    p = (2*b+1)**2 # - 1 + 1
    
    # start of the square has a new alignment so we need this
    s[p-2] += s[i]
    s[p-1] += s[i]
    
    # four sides of the square
    for h in range(4) :
    
      # walk along the side
      for g in range(m, 0, -1) :
      
        # finish condtion
        if s[i] > n :
          return s[i]
      
        # propagate starting at p
        # first 3 corners propagate to 5 positions, others 3
        for k in range(5 if g == CORNER and h < 3 else 3) :
          s[p+k] += s[i]
        
        # first 3 pre-corners or the last corner
        # must also propagate in this diagonal
        if g == PRECORNER and h < 3 or g == CORNER and h == 3 :
          s[i+2] += s[i]
      
        # propagate to next postion
        s[i+1] += s[i]
        
        # at the corners walk the propagation pointer 3 positions
        p += 3 if g == CORNER else 1
        
        i += 1
    
    # increase radius
    b += 1
    
  
print(run(n))
# print(s)
