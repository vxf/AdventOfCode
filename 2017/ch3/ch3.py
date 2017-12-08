#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vxf

import math

n = 368078
# n = 1024
# n = 12
# n = 23

# the squares always have an odd side length so we want to search only odd
# squares 2n+1
# we want to find the b right above n where (2b+1)**2 > n
b = math.floor((math.sqrt(n)-1)/2)

# and we also want to find the generating odd number
a = 2*b + 1

# we calculate the side length
m = 2 * (b + 1)

print(b + 1 + abs((n - (a*a)) % m - (b+1)))
