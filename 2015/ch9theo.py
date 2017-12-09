#!/usr/bin/env python3

from pprint import pprint

nodes = set()
distances = {}

with open("ch9input") as f :
  for l in f :
    l = l.strip()
    a, _, b, _, d  = l.split(" ")
    d = int(d)

    distances[(a, b)] = d
    distances[(b, a)] = d

    nodes.add(a)
    nodes.add(b)

def tsp(n1, visited, distance) :
  next = nodes - visited

  if not next:
    return distance

  return max(
    tsp(n2, visited | set([n2]), distances.get((n1, n2), 0) + distance)
    for n2 in next)

print(tsp(None, set(), 0))
