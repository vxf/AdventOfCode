#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

def chunks(a, n):
  x = 0
  r = []
  for b in a:
    r.append(b)
    x += 1
    if x >= n :
      yield r
      x = 0
      r = []
      

def printBuf(buf):
  for c in chunks(buf, 50) :
    print(''.join(['#' if a == 1 else ' ' for a in  c]))


with open('input', 'r') as f:
  buf = [0]*(50*6)
  
  j = 0

  for l in f :
    l = l.strip().split(' ')
    
    if l[0] == 'rect' :
      w, h = l[1].split('x')
      w, h = int(w), int(h)
      for y in range(h) :
        for x in range(w) :
          buf[x + y*50] = 1
    
    elif l[0] == 'rotate' :
      xy = int(l[2][2:])
      r = int(l[4])
      
      if l[1] == 'row' :
        row = [buf[xy*50 + ((i - r) % 50)] for i in range(50)]
        for i, c in enumerate(row) :
          buf[xy*50 + i] = c
          
      else : # 'column'
        col = [buf[((i - r) % 6)*50 + xy] for i in range(6)]
        for i, c in enumerate(col) :
          buf[i*50 + xy] = c
          
    printBuf(buf)
    print()
    j += 1
    #if j >= 4 :
    #  break

  printBuf(buf)  
  print(sum(buf))
