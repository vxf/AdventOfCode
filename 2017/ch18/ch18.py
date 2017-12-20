#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

SND, SET, ADD, MUL, MOD, RCV, JGZ = range(7)

instruction_set = [
  "snd",
  "set",
  "add",
  "mul",
  "mod",
  "rcv",
  "jgz"
]

def tok(i) :
  return instruction_set.index(i)

def run(vlen, prog) :
  pc = 0
  v = [0,] * vlen
  s = 0

  while pc >= 0 and pc < len(prog) :
    i, r1, r2, im = prog[pc]
    #print(v)
    #print(instruction_set[i])
    
    if   i == SND :
      s = v[r1]
      # print("-snd")
      # print(s)
    elif i == SET :
      v[r1] = r2 if im else v[r2]
    elif i == ADD :
      v[r1] += r2 if im else v[r2]
    elif i == MUL :
      v[r1] *= r2 if im else v[r2]
    elif i == MOD :
      v[r1] = v[r1]  % (r2 if im else v[r2])
    elif i == RCV :
      # print("-rcv")
      # print(s)
      if v[r1] != 0 :
        # print(s)
        return s
    elif i == JGZ :
      if v[r1] > 0 :
        pc +=  (r2 if im else v[r2]) - 1
    
    pc += 1
    
  return None

with open('input.txt', 'r') as f:
  v = []
  prog = []
  for l in f :
    l = l.rstrip().split()
    
    i = tok(l[0])
    
    r = l[1]
    if not r in v :
      v.append(r)
    r1 = v.index(r)
    
    r2 = 0
    im = False
    
    if len(l) > 2 :
      try:
        r2 = int(l[2])
        im = True
      except:
        r = l[2]
        if not r in v :
          v.append(r)
        r2 = v.index(r)
        im = False
        
    prog.append((i, r1, r2, im))
  
  #print(len(v))
    
  #print(prog)
  
  print(run(len(v), prog))
  
  
