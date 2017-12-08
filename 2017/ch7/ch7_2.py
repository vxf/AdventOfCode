#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

d = {}
def subweight(n) :
  w, s = d[n]
  
  if not s :
    return (n, w)
  
  wc = [subweight(c) for c in s]
  ww = [w for _, w in wc]
  if ww[1:] == ww[:-1] :
    return (n, w + sum(ww))
  else :
    # print(wc)
    #print(w)
    e = [key for key, value in wc if value == max(ww)]
    #print(d[e[0]][0])
    #print(max(ww, key=ww.count))
    print(d[e[0]][0] - (max(ww) - max(ww, key=ww.count)))
    raise Exception()

def findBase():
  e = {}
  
  e = {n: 0 for n in d}
  
  for n, t in d.items() :
    w, s = t
    
    for c in s :
      e[c] += 1
  
  return next(k for k, v in e.items() if v == 0)

with open('input.txt', 'r') as f:

  for l in f :
    l = l.split()
    
    p = l[0]
    s = "".join(l[3:])
    w = int(l[1][1:-1])
    
    s = [] if s == '' else s.split(",")
    
    d[p] = (w, s)

  base = findBase()
  # print(base)
  
  try:
    subweight(base) 
  except Exception: pass
      
    

      
