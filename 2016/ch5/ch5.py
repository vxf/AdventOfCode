#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

import sys
import hashlib
import itertools

doorid = 'ffykfhsq'

password = ''

for i in itertools.count():
  #print(doorid + str(i))
  h = hashlib.md5((doorid + str(i)).encode('utf-8')).hexdigest()
  #print(h[:5])
  if h[:5] == '00000' :
    password += h[5]
    print(password)
    if len(password) == 8 :
      break
  
print(password)  

