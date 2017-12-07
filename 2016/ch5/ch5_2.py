#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

import sys
import hashlib
import itertools

doorid = 'ffykfhsq'

password = ['_']*8

for i in itertools.count():
  #print(doorid + str(i))
  h = hashlib.md5((doorid + str(i)).encode('utf-8')).hexdigest()
  #print(h[:5])
  if h[:5] == '00000' :
    pos = int(h[5], 16)
    if pos > 7 or password[pos] != '_':
      continue
      
    password[pos] = h[6]
    
    print(password)
    if all([c != '_' for c in password]) :
      break
  
print("".join(password))  

